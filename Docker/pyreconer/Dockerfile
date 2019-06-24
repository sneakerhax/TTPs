FROM python:3

RUN mkdir PyReconer
COPY PyReconer.py /PyReconer
WORKDIR /PyReconer
RUN mkdir output
RUN wget https://github.com/OWASP/Amass/releases/download/3.0.4/amass_3.0.4_linux_amd64.zip && unzip amass_3.0.4_linux_amd64.zip && mv amass_3.0.4_linux_amd64 amass
RUN wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip && unzip aquatone_linux_amd64_1.7.0.zip -d aquatone
RUN wget https://download-chromium.appspot.com/dl/Linux_x64?type=snapshots -O chrome-linux.zip && unzip chrome-linux.zip
RUN apt update && apt -y install nmap

ENTRYPOINT ["python", "PyReconer.py"]