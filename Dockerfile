FROM python:3.8-buster
ADD . /octomongodb
WORKDIR /octomongodb
RUN apt-get update --allow-releaseinfo-change && apt-get install -y \
    openssl libssl-dev ssl-cert \
    iputils-ping python-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["bash", "runit.sh"]