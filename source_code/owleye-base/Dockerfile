FROM ubuntu:18.04

# COPY ./requirements.txt .
RUN apt-get update

# Installing basic linux tools
RUN apt install curl -y
RUN apt-get install unzip -y

# Installing Python 3.8 and pip3
RUN apt-get install python3.8 -y 
RUN apt install python3-pip -y
RUN pip3 install --upgrade pip

# Install Open CV and Pillow (Formely PIL)
RUN pip3 install opencv-python-headless
RUN pip3 install Pillow
RUN apt upgrade -y

# Install pytorch
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

# Copy source code and run script
WORKDIR /home
COPY ./OwlEye-main ./OwlEye-main

