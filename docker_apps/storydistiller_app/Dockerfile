FROM trevinwadu/bxer:storydistiller-base

RUN apt update && apt upgrade -y

# install python
RUN apt install wget -y
RUN apt-get install build-essential -y
RUN apt-get install zlib1g-dev -y
RUN apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
RUN tar -xvf Python-3.6.3.tgz
WORKDIR /opt/Python-3.6.3
RUN ./configure
RUN make
RUN make install

# install flask and boto3
WORKDIR /home/app
RUN pip3 install --upgrade pip
RUN pip3 install Flask
RUN pip3 install boto3

# install zip utils
RUN apt-get install zip gzip tar -y

# install aws 
RUN pip3 install awscli
COPY .aws /root/.aws

# temp directory for cache
RUN mkdir /home/tmp

EXPOSE 3002

# copy flask app
COPY ./app.py /home/app/app.py

# start flask app
CMD ["python3", "app.py"]