FROM python:3.8
MAINTAINER Carl Cauchi
COPY script /script
RUN pip install requests
WORKDIR /script
CMD [ "python", "./get-macaddressinfo.py" ]
