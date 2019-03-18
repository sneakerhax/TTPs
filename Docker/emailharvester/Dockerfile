# A dockerized version of the tool emailharvester by maldevel

FROM python:3

RUN git clone https://github.com/maldevel/EmailHarvester
RUN cd EmailHarvester
RUN pip install -r EmailHarvester/requirements.txt

WORKDIR /EmailHarvester
ENTRYPOINT ["python", "EmailHarvester.py"]
