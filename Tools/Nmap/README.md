# Nmap

A port scanning tools used for discovery and enumeration

## Installation
* Install [Nmap](https://nmap.org/download.html)
* Install [Nmap with Brew](https://formulae.brew.sh/formula/nmap)

## NSE script search

OSX

```
nse(){ find /usr/local/share/nmap/scripts/ -iname "*$1*" | cut -c32- | cut -d'.' -f1;i}
```

Linux

```
nse(){ find /usr/share/nmap/scripts/ -iname *$1* -printf '%P\n';}
```

Setup custom functions for searching nse scripts (Created by hecky)

```
nse search
```

Example usage of custom nse function

