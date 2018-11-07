#!/usr/bin/env python
# coding='utf-8'

import socket


# Get hostname
def chk_01():

    hostname_01 = socket.gethostname()
    print(hostname_01)

# Get IP
def chk_02():
    
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)

# Get IPs
def chk_03():
    
    ips = socket.gethostbyname_ex(socket.gethostname())
    print(ips)            # (hostname, aliaslist, ipaddrlist) == tuple
    print(ips[2])         # This is IPs == list
    print(ips[2][1])

# 
def chk_04():

    ips = socket.getaddrinfo(socket.gethostname(), None)
    print(ips)

# main
def main():

    # Checks
    print('chk 01') 
    chk_01()

    print('chk 02')
    chk_02()

    print('chk 03')
    chk_03()

    print('chk 04')
    chk_04()

if __name__ == '__main__':
    main()
