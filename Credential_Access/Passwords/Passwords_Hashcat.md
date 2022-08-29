# Passwords - Hashcat

```
hashcat -O -a 0 -m 5600 <hashes> <wordlist>
```

Cracking NTLMv2 captures from responder(with wordlist)

```
hashcat --show -m 5600 <hashes> <potfile>
```

Showing cracked passwords:
