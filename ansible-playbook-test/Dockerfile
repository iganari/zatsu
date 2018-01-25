FROM centos:7.4.1708

MAINTAINER iganari

ADD ./requirements.txt /tmp/requirements.txt

RUN yum install -y epel-release &&\
    rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
    yum clean all -y

RUN yum install --enablerepo=epel,remi -y python-devel \
                                          openssl-devel \
                                          gcc \
                                          libffi-devel &&\
    yum install --enablerepo=epel,remi -y python-pip

RUN pip install --upgrade pip &&\
    pip install -r /tmp/requirements.txt
