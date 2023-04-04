---
title: QEMU/KVM Machines Backup 
date: 2022-06-08 12:20
categories: [Sysadmin]
tags: [sysadmin, kvm, linux, backup, storage, borg]
---

# Prepare the machines
Having a lot of self hosted services is a fun hobby, but it also takes a lot of time to setup and configure every VM, so it's crucial to have a backup of your environment to restore everything you achieved in case of a data loss.
Here's how to do it with [Borg](https://www.borgbackup.org/).
First get a list of your virtual machines:
```bash
sudo virsh list --all
```
Shutdown every running machine, from virt-manager or with `sudo virsh shutdown MACHINE_NAME`, then dump the configuration of every machine (you can do this even if the VMs are running):
```bash
sudo virsh dumpxml MACHINE_NAME > /path/to/xml_folder/MACHINE_NAME.xml
```
Now, check where the `.qcow2` disk files are store (default location is `/var/lib/libvirt/images/`):

```bash
sudo virsh domblklist MACHINE_NAME
```

# Backup

Now that you have all your VMs files, let's setup a backup with Borg.
Borg uses repositories like git's to stored incremental, compressed and deduplicated backups. 
Before initializing a new repo you have to choose you're backup location: it can be a local folder, a folder on a removable disk, a network folder mounted with Samba or NFS or even a remote location using SSH. If you plan to use SSH you should setup an SSH key to access the server.
Let's init the repository:
```bash
# Mounted folder
borg init --encryption=repokey-blake2 /path/to/backup/folder

# SSH
borg init --encryption=repokey-blake2 ssh://user@ip:port//path/to/backup/folder
```
If you don't want encrypted backups or you want to use other encryption algorithms, you can specify `--encryption=none` for no encryption or `--encryption=repokey` to use SHA-256.

Lastly, let's create our first backup:

```bash

# Mounted Folder
sudo borg create --stats --progress --compression lz4 /path/to/backup_folder::{hostname}-{now} /path/to/disks_folder /path/to/xml_folder

# SSH
sudo borg create --stats --progress --compression lz4 ssh://user@ip:port//path/to/backup_folder::{hostname}-{now} /path/to/disks_folder /path/to/xml_folder
```

# Restore

<!-- To restore your backups, I recommend using [Vorta](https://vorta.borgbase.com/) to manage the backup repo and to mount it to a folder (CLI command `borg mount /path/to/repo /path/to/mountpoint`), copy the disk image you want to restore to its original location and then re-define the VM: -->

To restore your backups, mount the repo to a folder whit `borg mount /path/to/repo /path/to/mountpoint`, copy the disk image you want to restore (probably you have to do it with sudo `sudo cp src dest`) to its original location and then re-define the VM:

```bash
sudo virsh undefine MACHINE_NAME
sudo virsh define –file /path/to/xml_backup_folder/MACHINE_NAME.xml
```
Congratulations, you should have restored your VM successfully!

Thanks to [TSC](https://techsoftcenter.com/how-to-kvm-backup-and-restore-in-linux/) for the hints.