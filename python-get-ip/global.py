#!/usr/bin/env python
# coding='utf-8'

import requests


def inet_ip():

    top = requests.get('http://inet-ip.info')
    ip = requests.get('http://inet-ip.info/ip')
    json = requests.get('http://inet-ip.info/json')

    print('/     is :', top.text)
    print('/ip   is :', ip.text)
    print('/json is :', json.text)
   


def main():

    inet_ip()

if __name__ == '__main__':
    main()
