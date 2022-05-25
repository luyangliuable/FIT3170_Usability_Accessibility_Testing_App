# syntax=docker/dockerfile:1
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
RUN export DEBIAN_FRONTEND=noninteractive

RUN apt-get -yq update
RUN apt-get -yq upgrade


RUN apt-get -yq install sudo
RUN apt-get -yq install wget

RUN apt-get -yq install time

RUN apt-get -yq install unzip

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install openjdk-8-jdk

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install curl

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3.8-dev python3.8-distutils python3.8-venv
RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python3
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py


RUN wget --quiet https://github.com/souffle-lang/souffle/releases/download/1.7.1/souffle_1.7.1-1_amd64.deb
RUN apt-get install ./souffle_1.7.1-1_amd64.deb -y

RUN sudo DEBIAN_FRONTEND=noninteractive apt -yq install git

RUN wget --quiet https://github.com/izgzhen/android-platforms/releases/download/v0.1/android-tools-linux.zip
RUN unzip -q android-tools-linux.zip -d android-tools-linux
RUN yes | android-tools-linux/tools/bin/sdkmanager --licenses
RUN android-tools-linux/tools/bin/sdkmanager 'platforms;android-29'


RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -yq update
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install apt-transport-https curl gnupg -yqq
RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
RUN curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
RUN sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -yq update
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install sbt


ENV ANDROID_SDK /android-tools-linux/
RUN export ANDROID_SDK=$PWD/android-tools-linux

ENV ANDROID_SDK_ROOT /android-tools-linux/
RUN export ANDROID_SDK_ROOT=$PWD/android-tools-linux

ENV GTIME time
RUN export GTIME=time

ENV REPORT 1
RUN export REPORT=1

RUN wget --quiet https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py
RUN pip3 install --upgrade pip
RUN python3 get-poetry.py --version 1.0.2

WORKDIR /home
RUN git clone --recursive https://github.com/izgzhen/ui-checker.git

WORKDIR /home/ui-checker

RUN apt install make -y
RUN ~/.poetry/bin/poetry install
RUN rm -f .venv
RUN ln -s $(~/.poetry/bin/poetry env info --path) .venv