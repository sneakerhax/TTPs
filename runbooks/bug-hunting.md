# Bug Hunting

Bug hunting runbook

### Picking Bounty

* New programs will have more undiscovered bugs
* Very experienced hunters that have participated in programs may have found many of the low hanging fruit or have early access so keep this in mind
* Consider the scope vs your skill set
* If looking at an older program look for more unusual bugs such as XXE,SSRF,Sensitive information disclosure
* Choose programs with *.domain.com if possible for bigger scopes

### Getting Started

* Install Burp Suite(https://portswigger.net/burp/download.html)
* Install Mozilla(https://www.mozilla.org/en-US/firefox/new/)
* Install Foxy Proxy Standard(https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)
* See tools list (https://github.com/sneakerhax/Resources/blob/master/links/bug-hunting.md)
* Install Kali-Linux(optional - https://www.kali.org/downloads/)
* Install Nmap(can be found in Kali-Linux)
* Install subdomain brute forcer(can be found in Kali-Linux)
* Install directory brute forcer(can be found in Kali-Linux)

### Setting up Burp Suite

* Install Burp Suite from website(https://portswigger.net/burp/download.html)
* Install Mozilla Firefox(https://www.mozilla.org/en-US/firefox/new/)
* Install Foxy Proxy Standard(https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)
* Setup Burp Suite to user Foxy Proxy(https://support.portswigger.net/customer/portal/articles/1783066-configuring-firefox-to-work-with-burp)
* Configure Burp Suite SSL certificate(https://support.portswigger.net/customer/portal/articles/1783075-Installing_Installing%20CA%20Certificate.html)



## Hunting



### Recon

* Run sub-domain brute force if this is in scope to discover sudomains
	* sublister
	* fierce
	* recon-ng
  * For additional tools look [here](https://github.com/sneakerhax/Resources/blob/master/links/bug-hunting.md)

Examples:

```
python subbrute.py -s bitquark_subdomains_top100K.txt --type=A -P twilio.com
```

- Run Nmap scan on target(including subdomains) if this is in scope
	- Run nmap scan all ports


### Google Dorking

Google Dorking Examples:

```
site:site.com 
```

Search for specific site


* See more examples [here](http://www.googleguide.com/advanced_operators_reference.html)
* Also the Google Hacking Database can be found [here](https://www.exploit-db.com/google-hacking-database/)
	

### Probing app

* Visit app and sign up for access if necessary
	* Choose an email you have fully setup with 2factor and recovery
	* Choosing an email that contains the name of the bug bounty program(Bugcrowd, Hackerone)
* Read about app and manually review website
	* Visit functionality of website
	* Test user functionality 
* Test to see how the app reacts to basic functionality
	* Login and test login functionality
	* Test 404, 200, 500
	* Review cookies
* Check to see if application has change log
	* Google
	* Search website
* Spider website content
	* Manually review site with proxy running(Capture off)
	* Run Burp Suite spider(optional)
* Discover content(optional)
	* Use Burp Suite discover content(Only in Pro version)
	* Run dirb or dirbuster


### Data sources 

Sonar

Searching sonar data:

zgrep -a -F \.twilio.com *


### AWS

In Burpe keep ```.*amazon*.``` in scope

```
aws s3 ls s3://<repo-name>
``` 

Check s3 list permissions

```
aws s3 sync s3://repo
```

Get files locally for searching

```
aws s3 mv test.txt s3://bucket/
```

Check write permissions
