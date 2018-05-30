# Bug Hunting

A set of resources that can be used for bug hunting

### General
* [The Bug Hunters Methodology](https://github.com/jhaddix/tbhm) – Jason Haddix
* [Bug Bounty Reference](https://github.com/ngalongc/bug-bounty-reference) - ngalongc
* [Web Application Hackers Handbook 2](https://www.amazon.com/Web-Application-Hackers-Handbook-Exploiting/dp/1118026470) - Dafydd Stuttard, Marcus Pinto
* [Web Hacking 101](https://leanpub.com/web-hacking-101) - Peter Yaworski

### Recon

**Data/DNS/SSL/IP**

* [Recon-ng](https://bitbucket.org/LaNMaSteR53/recon-ng) (A full featured Web Reconnissance Framework) - Lanmaster53
* [Scan.io](https://scans.io) - Rapid7
  * [Sonar Reverse DNS](https://scans.io/study/sonar.rdns_v2)
  * [Sonar Forward DNS](https://scans.io/study/sonar.fdns_v2)
  * [Sonar SSL data](https://scans.io/study/sonar.ssl)
* [Crunchbase](https://www.crunchbase.com/)
* [Comodo Certificate Transparency List](https://crt.sh/) - Comodo
* [SSL Tools](http://ssltools.com/) - SSLTools
* [ARIN WHOIS](https://whois.arin.net/ui/) - ARIN
* [RIPE Database](https://apps.db.ripe.net/db-web-ui/#/query) - RIPE 
* [BGP Toolkit](https://bgp.he.net/) - Hurricane Electric

**DNS Brute Force**
* [Amass](https://github.com/caffix/amass) - caffix
* [Sublist3r](https://github.com/aboul3la/Sublist3r) (Fast subdomains enumeration tool for penetration testers) - aboul3la
* [Gobuster](https://github.com/OJ/gobuster) (Directory/file & DNS busting tool written in Go) - OJ
* [Altdns](https://github.com/infosec-au/altdns) (DNS brute force permutation generator) - Infosec-au
* [Domain](https://github.com/jhaddix/domain) (alt-dns & recon-ng automation script) - Jason Haddix
* [Massdns](https://github.com/blechschmidt/massdns) - blechschmidt
* [Fierce](http://tools.kali.org/information-gathering/fierce) (DNS brute forcer) - RSnake
* [Subbrute](https://github.com/TheRook/subbrute) (A DNS meta-query spider that enumerates DNS records, and subdomains) - TheRook
* [Knock](https://github.com/guelfoweb/knock) (Knock Subdomain Scan) - guelfoweb

**Port Scanners**
 * [Nmap](https://nmap.org/download.html) - Nmap Project
 * [Nmap NSE Scripts](https://nmap.org/nsedoc/) - Nmap Project
 * [Masscan](https://github.com/robertdavidgraham/masscan) - Robert Graham

**Screenshot**
 * [Eyewitness](https://github.com/ChrisTruncer/EyeWitness) - Chris Truncer

**Directory Brute Forcing**
* [Dirb](https://tools.kali.org/web-applications/dirb) - The Dark Raver
* GoBuster can also be used

**Parameter Brute Forcing**
* [Parameth](https://github.com/maK-/parameth) - maK-

### Github Searching
* [Gitrob](https://github.com/michenriksen/gitrob) - michenriksen
* [Gitrob Docker](https://github.com/awhitehatter/gitrob-docker) - awhitehatter
* [TruffleHog](https://github.com/dxa4481/truffleHog) - dxa4481
* [Comparing Commits](https://help.github.com/articles/comparing-commits-across-time/) - Github

### Docker

* [Docker Pentest List](https://github.com/awhitehatter/docker-pentest-lists) - awhitehatter
* [BruteSubs](https://github.com/anshumanbh/brutesubs) - anshumanbh

### Burp Suite Plugins
* [Burp Co2](http://burpco2.com/) (Burp Suite Extenstion) – Secure Ideas
* [Hunt](https://github.com/bugcrowd/HUNT) - Bugcrowd
* [Carbonator](https://portswigger.net/bappstore/bapps/details/e3a26fff8e1d401dade52f3a8d42d06b) - Integris Security
* [Vulners](https://github.com/vulnersCom/burp-vulners-scanner) (Called Software Vulnerability Scanner in BApp Store) - Vulners
* [BurpSmartBuster](https://github.com/pathetiq/BurpSmartBuster) - pathetiq
* [AuthMatrix](https://github.com/SecurityInnovation/AuthMatrix) - SecurityInnovation
* [xssValidator](https://github.com/nVisium/xssValidator) - nVisium
* [Burp_WP](https://github.com/kacperszurek/burp_wp) - kacperszurek

### Chrome plugins
* [Wappalyzer](https://chrome.google.com/webstore/detail/wappalyzer/gppongmhjkpfnbhagpmjfkannfbllamg?hl=en)
* [Builtwith](https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en)
* [Punkspider](https://chrome.google.com/webstore/detail/punkspider/ejdnmggbihgcgkgppokffmcfkhkdnlop?hl=en)
* [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)
* [Shodan](https://chrome.google.com/webstore/detail/shodan/jjalcfnidlmpjhdfepjhjbhnhkbgleap?hl=en-US)

### Firefox plugins
* [Wappalyzer](https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/)
* [Builtwith](https://addons.mozilla.org/En-us/firefox/addon/builtwith/)
* [Punkspider](https://addons.mozilla.org/en-US/firefox/addon/punkspider/)
* [Firebug](https://addons.mozilla.org/en-US/firefox/addon/firebug/)
* [Foxy Proxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)
* [Live HTTP header](https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/)
* [Tamper data](https://addons.mozilla.org/en-US/firefox/addon/tamper-data/)
* [Hackbar](https://addons.mozilla.org/en-US/firefox/addon/hackbar/)
* [Cookie Manager+](https://addons.mozilla.org/en-US/firefox/addon/cookies-manager-plus/)
* [Shodan](https://addons.mozilla.org/en-US/firefox/addon/shodan-firefox-addon/)

### SQLi
* [SQL Injection cheatsheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/) – Netsparker
* [SQL Injection cheatsheet](http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet) – Pentestmonkey
* [SQLmap Tamper Scripts](https://forum.bugcrowd.com/t/sqlmap-tamper-scripts-sql-injection-and-waf-bypass/423) (WAF bypass) – Jason Haddix

### XSS
* [XSS Filter Evasion Cheat Sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet) – Owasp
* [XSS All BruteLogic articles](https://gist.github.com/tfairane/f9b372ff9aeff61758e3eb71e7cbeba6) - BruteLogic
* [XSS Filter Bypass](https://gist.github.com/rvrsh3ll/09a8b933291f9f98e8ec) - rvrsh3ll
* [XSS Hunter](https://github.com/mandatoryprogrammer/xsshunter) (The XSS Hunter service - a portable version of XSSHunter.com) - mandatoryprogrammer
* [Sleepy Puppy](https://github.com/Netflix/sleepy-puppy) (Sleepy Puppy XSS Payload Management Framework)- Netflix
* [Ground Control](https://github.com/jobertabma/ground-control) (Mainly for debugging SSRF, blind XSS, and XXE vulnerabilities) - jobertabma
* [XSS Mind Map](https://github.com/jackmasa/XSS.png/tree/master) (A XSS mind map) - jackmasa
* [Ultimate XSS Polyglot](https://github.com/0xsobky/HackVault/wiki/Unleashing-an-Ultimate-XSS-Polyglot) (Unleashing an Ultimate XSS Polyglot) - Ahmed Elsobky

### SSTI(Server Side Template Injection)
* [TPLMap](https://github.com/epinna/tplmap) (Code and Server-Side Template Injection Detection and Exploitation Tool) - epinna

### Command Injection
* [Commix](https://github.com/commixproject/commix) (Automated All-in-One OS command injection and exploitation tool) - commixproject

### LFI/RFI
* [liffy](https://github.com/hvqzao/liffy) (Local file inclusion exploitation tool) – hvqzao

### Wordpress

* [WPScan](https://github.com/wpscanteam/wpscan) - wpscanteam

### CMS

* [CMSMap](https://github.com/Dionach/CMSmap) - Dionach

### Wordlists/Fuzzing
* [Seclists](https://github.com/danielmiessler/SecLists) – Daniel Miessler & Jason Haddix
* [FuzzDB](https://github.com/fuzzdb-project/fuzzdb) – FuzzDB-Project
* [DNSAll](https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056) - Jason Haddix
* [Wfuzz](https://github.com/xmendez/wfuzz/tree/master/wordlist) - Wfuzz
* [Payload All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings) - swissky
* [Paypal Test Credit Card Numbers](https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm) - Paypal
