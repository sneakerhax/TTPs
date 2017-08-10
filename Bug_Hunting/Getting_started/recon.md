# Recon


- Run Nmap scan on target(including subdomains) if this is in scope
	- Run nmap scan all ports(optional)

* For more information on Nmap scanning see [here](https://github.com/sneakerhax/Resources/blob/master/runbooks/Penetration_Testing/1.Recon/nmap.md)

* Run sub-domain brute force if this is in scope to discover sudomains
	* sublister
	* fierce
	* recon-ng
  * For additional tools look [here](https://github.com/sneakerhax/Resources/blob/master/links/bug-hunting.md)

Examples:

```
python subbrute.py -s bitquark_subdomains_top100K.txt --type=A -P site.com
```
