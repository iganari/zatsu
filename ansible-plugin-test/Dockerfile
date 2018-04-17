FROM ansible/centos7-ansible

MAINTAINER iganari


### setting Jp
RUN rm -rf /etc/localtime &&\
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime &&\
    echo 'LANG="ja_JP.utf8"' > /etc/locale.conf
