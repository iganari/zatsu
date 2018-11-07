#!/usr/bin/env python
# coding='utf-8'

import socket


# Get hostname
def chk_01():

    hostname_01 = socket.gethostname()
    print(hostname_01)

    return


# Get IP
def chk_02():
    
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)

    return


# Get IPs
def chk_03():
    
    ips = socket.gethostbyname_ex(socket.gethostname())
    print(ips)            # (hostname, aliaslist, ipaddrlist) == tuple
    print(ips[2])         # This is IPs == list
    print(ips[2][1])

    return

# 
def chk_04():

    ips = socket.getaddrinfo(socket.gethostname(), None)
    print(ips)

    return


def chk_05():

    ips = socket.getaddrinfo(socket.gethostname(), None)

    for line in range(len(ips)):
        print(ips[line])
   
    return
   

# main
def main():

    # Checks
    print('\nchk 01') 
    chk_01()

    print('\nchk 02')
    chk_02()

    print('\nchk 03')
    chk_03()

    print('\nchk 04')
    chk_04()

    print('\nchk 05')
    chk_05()

if __name__ == '__main__':
    main()
