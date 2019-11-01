FROM python:3.8
MAINTAINER Carl Cauchi
COPY script /script
COPY config /config
RUN pip install requests
WORKDIR /script
ENTRYPOINT ["python", "get-macaddressinfo.py"]