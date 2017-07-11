## SSL

```openssl s_client -connect sneakerhax.com:443 -showcerts```

View ssl certificate(Shows pem file)

```openssl s_client -connect sneakerhax.com:443 -showcerts | openssl x509 -noout -text```

View ssl certification information

```timeout 1 ssh -a -l ec2-user -v -o PubkeyAuthentication=no -o PasswordAuthentication=yes -o BatchMode=yes -o StrictHostKeyChecking=no ip_address 2>&1 | grep 'Authentications that can continue' ```

See supported authenication methods for SSH(Must have timeout installed(part of coreutils))
