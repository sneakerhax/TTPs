# Kali Linux - Re-install VMware Tools

```
sudo apt-get remove --auto-remove open-vm-tools-desktop
```

Remove open-vm-tools-desktop

```
sudo apt-get purge --auto-remove open-vm-tools-desktop
```

Purge open-vm-tools-desktop

```a
pt -y install open-vm-tools-desktop fuse
```

Re-install open-vm-tools-desktop

## References
* https://www.howtoinstall.co/en/ubuntu/trusty/open-vm-tools-desktop?action=remove
* https://docs.kali.org/general-use/install-vmware-tools-kali-guest
