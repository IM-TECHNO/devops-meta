FROM ubuntu:20.04


RUN apt-get update
RUN apt-get install -y libpq-dev 
RUN apt-get install -y python3-dev 
RUN apt-get install -y python3-pip 
RUN apt-get install -y git 
RUN apt-get clean
RUN cd /opt && git clone https://github.com/IM-TECHNO/devops-meta.git
RUN cd /opt/devops-meta && git pull

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r /opt/devops-meta/requirements.txt

WORKDIR /opt/devops-meta

EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
