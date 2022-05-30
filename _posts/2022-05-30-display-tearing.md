---
title: Fix X11 screen tearing 
date: 2022-05-30 18:20
categories: [linux]
tags: [X11, linux, display, intel]
---
> **Note**: this guide is for Intel Graphics only.
Using X11 I've always experienced screen tearing while watching videos or scrolling web pages. To improve the general experience and reduce the tearing, you can enable the "Tear Free" for the Intel Driver. First, if it doesn't exist, create the config file:
``` bash
mkdir /etc/X11/xorg.conf.d
sudo nano /etc/X11/xorg.conf.d/99-intel.conf
```
Then, paste the following lines and reboot:
```bash
Section "Device"
   Identifier  "Intel Graphics"
   Driver      "intel"
   Option      "AccelMethod" "sna"
   Option      "TearFree" "true"
EndSection
```
Now it should be almost tear free.