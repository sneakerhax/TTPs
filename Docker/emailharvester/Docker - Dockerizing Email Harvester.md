# Docker - Dockerizing Email Harvester

I was just hanging out on a Saturday night and I stumbled onto this tool called EmailHarvester. It runs on Python 3 and I still use Python 2.7 and didn’t want to deal with virutualenv and whatnot. I decided it might be a good time to learn how to Dockerize tools. This is nothing mind blowing or new but I haven’t done this before.

### Creating the Dockerfile

First thing that needs to be done is to build a Dockerfile that will used to build the image (Can be found [here](https://github.com/sneakerhax/Runbooks/blob/master/Docker/emailharvester/Dockerfile)):

```
# A dockerized version of the tool emailharvester by maldevel

FROM python:3

RUN git clone https://github.com/maldevel/EmailHarvester
RUN cd EmailHarvester
RUN pip install -r EmailHarvester/requirements.txt

WORKDIR /EmailHarvester
ENTRYPOINT ["python", "EmailHarvester.py"]
```

Here is the break down line by line:

1. Grabs the Docker image for Python3 (Line 3)
2. Runs a command that will clone the EmailHarvester repo (line 5)
3. Runs a command to change directory into the newly clone EmailHarvester folder (line 6)
4. Runs a command to pip install all dependencies from the requirement.txt file (line 7)
5. Changing the working directory so that all further commands run from the location /EmailHarvester (line 9)
6. Uses Entrypoint to set the action taken when the container is executed. Allows you to pass arguments (line 10)

For more information the documentation can be found [here](https://docs.docker.com/engine/reference/builder/)

### Building the Docker image

To build the image run  the following command:

```
docker build -t emailharvester .
```

Additionally you can add a label to the name (-t) by doing name:label. If you don’t add a label the default will be “latest”.

For more information the documentation can be found [here](https://docs.docker.com/engine/reference/commandline/build/)

### Running the Docker image

To run the Docker image do the following:

```
$ docker run -it emailharvester -d domain.com
[+] User-Agent in use: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1
[+] Searching everywhere
[+] Searching in ASK: 10 results
[+] Searching in ASK: 20 results
[+] Searching in ASK: 30 results
[+] Searching in ASK: 40 results
[+] Searching in ASK: 50 results
```

This runs the docker image in interactive mode and takes everything after the image name as an argument.

For more information the documentation can be found [here](https://docs.docker.com/engine/reference/commandline/run/)

### Conclusion

So there you go a Dockerized tool. This makes it really easy to deal with dependencies. For example you can send the image to a friend and they can run it with ease as long as they have Docker. It doesn’t matter what kind of system they are running. I think all tools should come with a Dockerfile to deal with dependency issues.
