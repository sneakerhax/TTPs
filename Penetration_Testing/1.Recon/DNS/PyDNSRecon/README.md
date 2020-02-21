# PyDNSRecon

A tool that collects DNS records from the 3 resources I found most useful and creates a unique list

### Setup

Add your Censys.io censys API ID and secret (Line 9,10):
```
# Censys.io access
censys_API_ID = "<censys_API_ID>"
censys_secret = "<censys_secret>"
```

Setup the path to the amass binary (Line 14):
```
amass_binary = "amass"
```

Additionally you need to download Sonar FDNS data from [here](https://opendata.rapid7.com/sonar.fdns_v2/2019-06-21-1561158121-fdns_cname.json.gz) and place it in the same directory as the Python script. Download the updated scan and change the sonar_fdns_data (Line 19) variable for the latest data:
```
sonar_fdns_data = "2019-06-21-1561158121-fdns_cname.json.gz"
```


### Example usage

```
$ python3 PyDNSRecon.py site.com
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
[+] Running crt.sh search forgrammarly.io
[+] Printing 5 discovered DNS records
dev.site.com
staging.site.com
admin.site.com
test.site.com
beta.site.com
```
