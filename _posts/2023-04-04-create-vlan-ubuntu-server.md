---
title: How to create VLANs in Ubuntu Server
date: 2023-04-04 16:10
categories: [Networking]
tags: [linux, networking, netplan, homelab]
---

My self-hosted services are growing in number, so the network configuration has to keep up in terms of security and scalability. My server has a quad port NIC connected to a managed switch which supports 802.1Q VLANs, so in this post I'll show you how to create VLANs in Ubuntu Server using *netplan*:
1. Using a terminal, open the netplan configuration file located inside `/etc/netplan` 
```bash
# In my case
sudo nano /etc/netplan/00-installer-config.yaml
```

2. Choose an available interface (you can get a list  with the command `ip -c a`) and create a new VLAN under the tag `vlans`. In this case I'm creating just one new virtual interface named `vlan.300` with a VLAN ID equal to `300` associated with the interface `eno3`, but you can create as many VLANs as you want (VLAN IDs ranges between `0` and `4095`)
```yaml
network:
	ethernets:
		eno3:
			dhcp4: false
	vlans:
		vlan.300:
			id: 300
			link: eno3
			dhcp4: false
version: 2
renderer: networkd
```

3. Now check your new configuration syntax and apply the changes
```bash
yamllint /etc/netplan/yourconfig
sudo netplan apply
# or better
sudo reboot
```

Now typing `ip -c a` you should see the newly create interface among the old ones.
Remember to connect the selected physical interface to a tagged/trunked port on your switch.
