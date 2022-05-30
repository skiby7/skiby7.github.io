---
title: Manage Drive Images
date: 2022-05-30 19:20
categories: [Sysadmin]
tags: [linux, administration, sysadmin]
---
When working on multiple projects or you have a nice setup, it is useful to backup the entire boot drive in a `.img` file either to restore a perfectly working environment (for example after a drive failure or a catastrophic update 🙃) or to switch between multiple projects using the same drive (however beware drive wearing if you use an SSD or an SD card).
Here's how to do it:

>**Note**: *replace /dev/sda with the drive you want to backup/restore!*

```bash
# Backup
sudo dd bs=4M if=/dev/sda of=Drive.img

# Restore
sudo dd bs=4M if=Drive.img of=/dev/sda

```

If you want to use compressed images (recommended):

```bash
# Backup
sudo dd bs=4M if=/dev/sda | gzip > Drive.img.gz

# Restore
gunzip --stdout Drive.img.gz | sudo dd bs=4M of=/dev/sda
```
