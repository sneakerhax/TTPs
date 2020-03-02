# PyDNSRecon

A tool that collects DNS records from the 4 resources and tools that create unique findings

### Setup

Add your Censys.io censys API ID and secret (Line 9,10):
```
# Censys.io access
censys_API_ID = "<censys_API_ID>"
censys_secret = "<censys_secret>"
```

### Running with Docker

Building Docker image

```
docker build -t pydnsrecon .
```

Running Docker image
```
docker run -it pydnsrecon <target>
```


### Example usage

```
$ docker run -it PyDNSRecon.py site.com
    ____        ____  _   _______ ____
   / __ \__  __/ __ \/ | / / ___// __ \___  _________  ____
  / /_/ / / / / / / /  |/ /\__ \/ /_/ / _ \/ ___/ __ \/ __ \
 / ____/ /_/ / /_/ / /|  /___/ / _, _/  __/ /__/ /_/ / / / /
/_/    \__, /_____/_/ |_//____/_/ |_|\___/\___/\____/_/ /_/
      /____/

by: sneakerhax

[+] Running Censys.io certificate search on site.com
[+] Running Amass on site.com
[+] Running Zgrep on Sonar fdns data for site.com
[+] Running crt.sh search site.com
[+] Printing 5 discovered DNS records
dev.site.com
staging.site.com
admin.site.com
test.site.com
beta.site.com
```
