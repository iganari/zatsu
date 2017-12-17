#!/bin/bash

set -x

yum_install_ansible()
{

  ### add reop
  yum install -y epel-release
  rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
  sed -i 's/enabled=1/enabled=0/g' /etc/yum.repos.d/epel.repo
 
  ### install python development tools
  yum clean all -y
  yum install --enablerepo=epel,remi -y python-devel openssl-devel gcc libffi-devel
  yum install --enablerepo=epel,remi -y python-pip
 
  ### install ansible in Python2
  pip install --upgrade pip
  pip install -r requirements.txt

}

### install ansible
yum_install_ansible

rm -rfv *.retry
