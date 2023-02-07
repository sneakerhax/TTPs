# Gobuster

**Description:** This entry describes how to use gobuster to discover website content

**Requirements:** gobuster

## Running Gobuster to discover website content

```
gobuster -u <url> -w <wordlist> -t 50 -fw -s 20
```

Brute force with 50 threads and only list status code 200
  
## References
* [Gobuster Github](https://github.com/OJ/gobuster)