# Setting up Docker auto completion on OSX Monterey/M1 (zsh)


## Fetching the completion files

```
mkdir -p ~/.zsh/completion
curl -L https://raw.githubusercontent.com/docker/docker-ce/master/components/cli/contrib/completion/zsh/_docker > ~/.zsh/completion/_docker
curl -L https://raw.githubusercontent.com/docker/machine/master/contrib/completion/zsh/_docker-machine > ~/.zsh/completion/_docker-machine
curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose
```

## Linking the completion files

```
mkdir -p ~/.zsh/completion
ln -s /Applications/Docker.app/Contents/Resources/etc/docker.zsh-completion ~/.zsh/completion/_docker
ln -s /Applications/Docker.app/Contents/Resources/etc/docker-machine.zsh-completion ~/.zsh/completion/_docker-machine
ln -s /Applications/Docker.app/Contents/Resources/etc/docker-compose.zsh-completion ~/.zsh/completion/_docker-compose
```

## Add to your .zshrc file

```
autoload -Uz compinit
fpath=(~/.zsh/completion $fpath)
compinit -i
```

## Resources
* https://daten-und-bass.io/blog/fixing-docker-command-auto-completion-in-mac-os-catalina/

# Setting up Kubernetes auto completion on OSX (zsh)

```
kubectl completion zsh
```

Generate the auto completion script

```
source <(kubectl completion zsh)
```

Add this line to .zshrc

## Resources
* https://kubernetes.io/docs/tasks/tools/install-kubectl/
