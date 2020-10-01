#!/usr/bin/python3.8

import ftplib

def get(ftp):
    try:
        dirlist=ftp.nlst()
        print('listing the contents ')
        retlist=[]
        for file in dirlist:
            fn=file.lower()
            if '.php' in fn or '.html' in fn or '.asp' in fn :
                print ('found default file ')
                retlist.append(file)
                return retlst
            else:
                print('no default page found')
    except :
        print('not listing')
        return
host='192.168.43.75'
user='msfadmin'
password='msfadmin'
ftp=ftplib.FTP(host)
try:
    ftp.login(user,password)
    print('Logining')
    get(ftp)
except Exception as e:
    print(str(e))