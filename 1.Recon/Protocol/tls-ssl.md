# TLS, SSL

**Description:** This entry describes how to collect SSL/TLS certificate information

**Requirements:** openssl, timeout

## Collecting ssl/tls certificate information

```
openssl s_client -connect sneakerhax.com:443 -showcerts
```

View ssl certificate(Shows PEM file)

```
openssl s_client -connect sneakerhax.com:443 -showcerts | openssl x509 -noout -text
```

View ssl certificate(x509) information

```
timeout 1 ssh -a -l ec2-user -v -o PubkeyAuthentication=no -o PasswordAuthentication=yes -o BatchMode=yes -o StrictHostKeyChecking=no <target> 2>&1 | grep 'Authentications that can continue'
```

See supported authentication methods for SSH(Must have timeout installed(part of coreutils))
  
## References
* [OpenSSL CLI Docs](https://wiki.openssl.org/index.php/Command_Line_Utilities)



