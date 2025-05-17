---
title: How to manage Wireguard peers access to LAN
date: 2023-04-15 23:15
categories: [Networking]
tags: [networking, wireguard, linux, iptables, firewall]
---

I spent an entire day trying to figure out how to restrict Wireguard clients access to the LAN network and here's what I found.

> *Credits to qdm12 and samboman who discussed this topic on [this](https://gist.github.com/qdm12/4e0e4f9d1a34db9cf63ebb0997827d0d) gist.*

When you enable or disable a new interface (`wg-quick up/down wgX`), runs the commands defined inside `/etc/wireguard/wgX.conf`:

```text
PreUp=Command executed before enabling the interface
PostUp=Command executed after the interface is up
PostUp=You can also define multiple commands

PreDown=Command executed before disabling the interface
PostDown=Command executed after the interface is down
```

Since there are a few commands we need to enter, we will simply create 2 scripts and set the configuration variables to `PostUp=/path/to/PostUp.sh` and `PostDown=/path/to/PostDown.sh`.
Before starting, here's my setup:

* Server network: `172.16.30.0/30`

* Network interface: `eth0`

* Wireguard network: `10.13.13.0/24`

* Allowed IPs: `0.0.0.0/0, ::/0`

**Important Note:** you can run Wireguard *bare-metal* or inside a docker container (I recommend [wg-easy](https://hub.docker.com/r/weejewel/wg-easy)), so you have to set the `MASQUERADE_INTERFACE` variable accordingly. On bare-metal installations, you can find the active interface by running `ip -c a` in a terminal, while on docker deployments it should be `eth0` (otherwise, you can open the container terminal with `docker exec -it <container-name> /bin/bash` and then run `ip -c a`).

# `PostUp.sh`

```bash
WIREGUARD_INTERFACE=wg0
WIREGUARD_LAN=10.13.13.0/24
WIREGUARD_FULL_ACCESS=10.13.13.0/25
WIREGUARD_GUEST=10.13.13.128/25
MASQUERADE_INTERFACE=eth0

iptables -t nat -I POSTROUTING -o $MASQUERADE_INTERFACE -j MASQUERADE -s $WIREGUARD_LAN

# Add a WIREGUARD_wg0 chain to the FORWARD chain
CHAIN_NAME=WIREGUARD_$WIREGUARD_INTERFACE
iptables -N $CHAIN_NAME
iptables -A FORWARD -j $CHAIN_NAME

# Accept related or established traffic
iptables -A $CHAIN_NAME -o $WIREGUARD_INTERFACE -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

# TRUSTED
# Accept traffic from any trusted IP address
iptables -A $CHAIN_NAME -s $WIREGUARD_FULL_ACCESS -i $WIREGUARD_INTERFACE -j ACCEPT

# GUEST
# Drop traffic to your any private IP address
iptables -A $CHAIN_NAME -s $WIREGUARD_GUEST -i $WIREGUARD_INTERFACE -d 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16 -j DROP

# Accept outgoing connections to any IP address (public because of rule above)
iptables -A $CHAIN_NAME -s $WIREGUARD_GUEST -i $WIREGUARD_INTERFACE -d 0.0.0.0/0 -j ACCEPT

# Drop everything else coming through the Wireguard interface
iptables -A $CHAIN_NAME -i $WIREGUARD_INTERFACE -j DROP

# Return to FORWARD chain
iptables -A $CHAIN_NAME -j RETURN
```

Peers connected to the `FULL_ACCESS` subnet can connect to the services hosted on the local network, while the peers on the GUEST subnet can only access to the public IP addresses. Note that you can also define other rules to filter traffic for specific peers:

```bash
# DNS (allow access to LAN services)
iptables -A $CHAIN_NAME -s 10.13.13.3 -i $WIREGUARD_INTERFACE -d 192.168.1.1 -p udp --dport 53 -j ACCEPT
# Drop traffic to your any private IP address
iptables -A $CHAIN_NAME -s 10.13.13.3 -i $WIREGUARD_INTERFACE -d 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16 -j DROP
# Accept outgoing connections to HTTP(S) ports to any IP address (filter access to public services)
iptables -A $CHAIN_NAME -s 10.13.13.3 -i $WIREGUARD_INTERFACE -d 0.0.0.0/0 -p tcp -m multiport --dports 80,443 -j ACCEPT
```
# `PostDown.sh`

To delete the rules after the interface is disabled:

```bash
WIREGUARD_INTERFACE=wg0
WIREGUARD_LAN=10.13.13.0/24
MASQUERADE_INTERFACE=eth0
CHAIN_NAME="WIREGUARD_$WIREGUARD_INTERFACE"

iptables -t nat -D POSTROUTING -o $MASQUERADE_INTERFACE -j MASQUERADE -s $WIREGUARD_LAN

# Remove and delete the WIREGUARD_wg0 chain
iptables -D FORWARD -j $CHAIN_NAME
iptables -F $CHAIN_NAME
iptables -X $CHAIN_NAME
```

# Bonus: setup `PostUp` and `PostDown` in wg-easy

If you're running wg-easy, you just need to create the scripts inside the `config` folder and set the environmental variables accordingly. Here's my `docker-compose.yml` (`post-up.sh` and `post-down.sh` are placed inside `config`):

```yml
version: "3.8"
services:
  wg-easy:
    image: weejewel/wg-easy
    container_name: wg-easy
    environment:
      - WG_HOST=public ip address or ddns
      - PASSWORD=web-ui-password
      - WG_PORT=<external-port>
      - WG_DEFAULT_ADDRESS=10.13.13.x # Wireguard LAN, it must terminate with .x
      - WG_DEFAULT_DNS=9.9.9.9,149.112.112.112
      - WG_MTU=1420
      - WG_ALLOWED_IPS=0.0.0.0/0, ::/0
      - WG_POST_UP=/etc/wireguard/post-up.sh
      - WG_POST_DOWN=/etc/wireguard/post-down.sh
    volumes:
      - ./config:/etc/wireguard
    ports:
      - <external-port>:51820/udp
      - 8080:51821/tcp
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    sysctls:
      - net.ipv4.ip_forward=1
      - net.ipv4.conf.all.src_valid_mark=1
    restart: unless-stopped
```
