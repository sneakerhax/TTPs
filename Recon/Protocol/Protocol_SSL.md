# Protocol - SSL

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
