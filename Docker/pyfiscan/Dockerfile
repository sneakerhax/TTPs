# A dockerized version of the tool pyfiscan by fgeek

FROM python:3

RUN git clone https://github.com/fgeek/pyfiscan.git && cd pyfiscan
RUN pip3 install -r pyfiscan/requirements.lst

ENTRYPOINT ["python", "pyfiscan/pyfiscan.py"]
