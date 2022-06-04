---
title: Fix X11 Screen Tearing 
date: 2022-05-30 18:20
categories: [Linux]
tags: [X11, linux, display, intel]
---
> **Note**: *this guide is for Intel Graphics only.*

Using X11 I've always experienced screen tearing while watching videos or scrolling web pages. To improve the general experience and reduce the tearing, you can enable the "Tear Free" option for the Intel Driver. Firstly, if it doesn't exist, create the config file:
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
Now you should have an almost tear free experience.