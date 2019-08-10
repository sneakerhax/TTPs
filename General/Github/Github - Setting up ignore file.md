# Github - Setting up ignore file

### Ignore all .DS_store files:

Create global git ignore file
```
echo .DS_Store >> ~/.gitignore_global
```

Set global git ignore file
```
git config --global core.excludesfile ~/.gitignore_global
```
