FROM ubuntu:16.04

ENV PYTHONUNBUFFERED=1

# install basic linux tools
RUN apt-get update -y
RUN apt install curl -y
RUN apt-get install unzip -y

#install jdk 8
RUN apt install openjdk-8-jdk -y

# install python 2.7 and required python dependencies
RUN apt-get install python-minimal -y && \
    curl "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    pip install pip==18.1 && \
    pip install treelib && \
    pip install opencv-python==3.4.3.18 && \
    apt install python-scrapy -y

# install apk tool
WORKDIR /usr/local/bin
RUN curl -sLO https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool && chmod +x apktool
RUN curl -sL -o apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.4.1.jar && chmod +x apktool.jar

# install android sdk (platform-tools)
RUN mkdir -p /usr/local/android-sdk \
    && cd /usr/local/android-sdk/ \
    && curl -OL https://dl.google.com/android/repository/platform-tools-latest-linux.zip \
    && unzip platform-tools-latest-linux.zip \
    && rm -f platform-tools-latest-linux.zip \
    && ln -s /usr/local/android-sdk/platform-tools/adb /usr/bin/adb \
    && export PATH=/usr/local/android-sdk/platform-tools:${PATH} \
    && echo "export PATH=/usr/local/android-sdk/platform-tools:${PATH}" >> /etc/profile

# install aapt
RUN apt install aapt -y

# set directory to root
WORKDIR /

