#!/bin/usr/python3.8 

import ftplib
import argparse

def anon(host):
    try:
        ftp=ftplib.FTP(host)
        ftp.login('anonymous','me@yours.com')
        print('login succeded')
        ftp.quit
    except Exception as e:
        print (str(e))
        

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-H','--host',action='store',dest='host',help='specify the host ip or name ')
    args=parser.parse_args()
    host=args.host
    if host==None :
        print('specify the host ')
    else:
        anon(host)
if __name__=='__main__':
    main()
   