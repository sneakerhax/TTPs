# Docker - PyReconer

```docker build -t pyreconer .```

Building Docker image (Chromium download takes a few minutes)

```docker run -it pyreconer <target>```

Running Docker container

### Sample Usage:

```
$ docker run -it pyreconer scanme.nmap.org
    ____        ____
   / __ \__  __/ __ \___  _________  ____  ___  _____
  / /_/ / / / / /_/ / _ \/ ___/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / _, _/  __/ /__/ /_/ / / / /  __/ /
/_/    \__, /_/ |_|\___/\___/\____/_/ /_/\___/_/
      /____/

by: sneakerhax

[+] Running amass on scanme.nmap.org

OWASP Amass v3.0.4                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
1 names discovered - dns: 1
--------------------------------------------------------------------------------
ASN: 63949 - LINODE-AP Linode
	45.33.32.0/24     	1    Subdomain Name(s)
scanme.nmap.org

[+] Running nmap on output/amass_results.txt

Starting Nmap 7.40 ( https://nmap.org ) at 2019-07-08 21:34 UTC
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up, received user-set (0.030s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
Reason: 996 resets
PORT      STATE SERVICE    REASON
22/tcp    open  ssh        syn-ack ttl 49
80/tcp    open  http       syn-ack ttl 50
9929/tcp  open  nping-echo syn-ack ttl 50
31337/tcp open  Elite      syn-ack ttl 49

Nmap done: 1 IP address (1 host up) scanned in 1.73 seconds

[+] Converting Nmap XML to CSV

[+] The file output/nmap_results.csv does not exist. New file created!


[+] Running aquatone on output/nmap_results.xml
aquatone v1.7.0 started at 2019-07-08T21:34:37Z

Targets    : 2
Threads    : 2
Ports      : 80, 443, 8000, 8080, 8443
Output dir : output

http://scanme.nmap.org/: 200 OK
http://scanme.nmap.org/: 200 OK
http://scanme.nmap.org/: screenshot successful
http://scanme.nmap.org/: screenshot successful
Calculating page structures... done
Clustering similar pages... done
Generating HTML report... done

Writing session file...Time:
 - Started at  : 2019-07-08T21:34:37Z
 - Finished at : 2019-07-08T21:34:41Z
 - Duration    : 5s

Requests:
 - Successful : 2
 - Failed     : 0

 - 2xx : 2
 - 3xx : 0
 - 4xx : 0
 - 5xx : 0

Screenshots:
 - Successful : 2
 - Failed     : 0

Wrote HTML report to: output/aquatone_report.html
```

### List of 3rd party tools:

* [Amass](https://github.com/OWASP/Amass) - OWASP
* [Nmap](https://nmap.org/) - Fyador and contributors
* [Aquatone](https://github.com/michenriksen/aquatone) - michenriksen
* [Nmap-Scan-to-CSV](https://github.com/laconicwolf/Nmap-Scan-to-CSV) - laconicwolf
