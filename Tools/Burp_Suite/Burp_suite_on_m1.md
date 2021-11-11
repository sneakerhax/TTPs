# Running Burp Suite on M1

Instructions for running the current Burp Suite MacOS (Intel) version on M1 Apple Silicon

## Downloading Burp Suite

https://portswigger.net/burp/releases/community/latest

Download the MacOS (Intel) version and run the install

## Creating a Rosetta Terminnal

1. Open the applications folder. Right click your terminal and choose "Duplicate"

2. Rename the terminal Rosetta-Terminal

3. Right click the newly created Rosetta-Terminal and choose "Get Info"

4. Click the checkbox for the option inside the info window called "Open using Rosetta"

5. This terminal will now run using Rosetta. You can verify by opening a terminal and running `uname -a`

## Running Burp Suite

```
open /Applications/<burp_suite>.app
```

Open your Rosetta terminal and run the following
