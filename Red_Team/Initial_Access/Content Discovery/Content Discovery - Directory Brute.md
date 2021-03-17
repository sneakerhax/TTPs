# Content Discovery - Directory Brute

```dirb http://<url> <wordlist> -w -N 404```

Brute force with dirb and ignore 404 reponses

```gobuster -u <url> -w <wordlist> -t 50 -fw -s 20```

Brute force with 50 threads and only list status code 200
