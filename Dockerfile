FROM python:3.8
MAINTAINER Carl Cauchi
COPY script /script
WORKDIR /script
CMD [ "python", "./get-macaddressinfo.py" ]