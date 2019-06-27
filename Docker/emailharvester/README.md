# Docker - EmailHarvester

```docker build -t emailharvester .```

Building Docker image

```docker run -it emailharvester <target>```

Running Docker container

```docker run -it emailharvester <target> -r dogpile```

If you get "Connection Aborted." error exclude dogpile plugin
