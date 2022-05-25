FROM trevinwadu/bxer:owleye-base

# install zip utils
RUN apt-get install zip gzip tar -y

# install flask and boto3
WORKDIR /home/app
RUN pip3 install --upgrade pip
RUN pip3 install Flask
RUN pip3 install boto3

# install aws 
RUN pip3 install awscli
COPY .aws /root/.aws

# temp directory for cache
RUN mkdir /home/tmp

# copy flask app
COPY ./app.py /home/app/app.py

CMD ["python3", "app.py"]