---
title: How to resize qcow2 disks
date: 2023-04-11 23:22
categories: [Sysadmin]
tags: [sysadmin, kvm, linux, qcow2, storage]
---

Here's a brief guide on how to resize qcow2 disks used by KVM virtual machines.
First shutdown the VM:
```bash
sudo virsh shutdown <machine-name>
```

Backup the disk to resize and then expand it (in this case I increase the size by 10 GB):
```bash
cp disk.qcow2 disk.qcow2.bup
sudo qemu-img resize disk.qcow2 +10G
sudo virsh start <machine-name>
```

Now on the guest machine resize the partition:
```bash
# Assuming that you are using lvm volumes with vda3 the root partition
sudo growpart /dev/vda 3
sudo reboot
# Open lvm
sudo lvm
# Use the lvextend command to expand the logical volume
lvm> lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
# Resize the filesystem
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```

Done!
