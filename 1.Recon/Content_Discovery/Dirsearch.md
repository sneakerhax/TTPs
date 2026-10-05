# Dirsearch

**Description:** This entry describes how to use dirsearch to discover website content

**Requirements:** dirsearch

## Building Dirsearch with Docker from remote source

```
docker build -t dirsearch https://github.com/maurosoria/dirsearch.git
```

Build Dirsearch without pulling down the repo to your system

## Running Dirsearch with Docker to discover website content

```
docker run -it -v <path_to_wordlist>:/<filename> -it dirsearch -w /<filename> -u <target>
```

Brute force with wordlist using dirsearch. Optionally add -i and specify status codes to filter on.
  
## References
* [Kali Tool - dirsearch](https://www.kali.org/tools/dirsearch/)
* [Github - Dirsearch](https://github.com/maurosoria/dirsearch)
