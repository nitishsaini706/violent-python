#!/usr/bin/python3

import pexpect
import argparse
import socket 

Prompt=['#','\$','>>>','>']

def connect(user,host,password):
    ssh_key='Sure about continuing connection? '
    con='ssh\t'+user+'@'+host
    child=pexpect.spawn(con)
    ret=child.expect([pexpect.TIMEOUT,ssh_key,'[P|p]ssword :'])
    if ret==0:
        print('TIMEOUT!!')
        return 
    if ret==1:
        child.sendline('yes')
        ret-child.expect([pexpect.TIMEOUT,'[P|p]password:'])
        if ret==0:
             print('CONNECTION ERROR')
    child.sendline(password)
    child.expect(Prompt)
    return child
   

def command(child):
    child.sendline('cat /etc/shadow |grep root')
    child.expect(Prompt)
    print (child.before)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-H','--host',dest='host',action='store',help='Enter host name ')
    parser.add_argument('-p','--password',dest='password',action='store',help='Enter password')
    parser.add_argument('-u','--user',dest='user',action='store',help='specify the user')
   # parser.add_argument('-c','--command',dest='cmd',action='store',help='specify the command')
    args=parser.parse_args()
    user=args.user
    host=args.host
    password=args.password
  # cmd=args.cmd
    if (user=='NULL') or (host=='NULL') or (password=='NULL') :
        print('specify user ,host,password')
    else:
        child=connect(user,host,password)
        command(child)


if __name__=='__main__':
    main()

    

