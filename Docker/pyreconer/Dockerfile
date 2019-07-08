FROM python:3

RUN mkdir PyReconer
COPY PyReconer.py /PyReconer
WORKDIR /PyReconer
RUN mkdir output
RUN wget https://github.com/OWASP/Amass/releases/download/3.0.4/amass_3.0.4_linux_amd64.zip && unzip amass_3.0.4_linux_amd64.zip && mv amass_3.0.4_linux_amd64 amass
RUN wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip && unzip aquatone_linux_amd64_1.7.0.zip -d aquatone
RUN wget https://download-chromium.appspot.com/dl/Linux_x64?type=snapshots -O chrome-linux.zip && unzip chrome-linux.zip
RUN apt update && apt -y install nmap
RUN git clone https://github.com/laconicwolf/Nmap-Scan-to-CSV
RUN apt install -yq --no-install-recommends libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 libnss3 

ENTRYPOINT ["python", "PyReconer.py"]
