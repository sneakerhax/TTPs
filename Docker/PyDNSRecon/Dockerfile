FROM python:3

RUN mkdir PyDNSRecon
COPY PyDNSRecon.py /PyDNSRecon
WORKDIR /PyDNSRecon
RUN wget https://github.com/OWASP/Amass/releases/download/v3.4.4/amass_v3.4.4_linux_amd64.zip && unzip amass_v3.4.4_linux_amd64.zip && mv amass_v3.4.4_linux_amd64 amass
RUN wget https://opendata.rapid7.com/sonar.fdns_v2/2020-02-23-1582480801-fdns_cname.json.gz && mv 2020-02-23-1582480801-fdns_cname.json.gz sonar.json.gz
RUN pip install requests

ENTRYPOINT ["python", "PyDNSRecon.py"]
