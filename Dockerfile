FROM centos:6.7
MAINTAINER Juan Monetti <juanmonetti@gmail.com>

RUN yum update -y; yum clean all
RUN yum install -y epel-release; yum clean all

RUN yum install -y python-pip; yum clean all

ADD . src/
RUN cd src/; ls -ls;pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "/forecast/server.py"]
