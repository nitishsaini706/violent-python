
import socket
import argparse

def con(tgthost,tgtport):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        try:
            g=socket.gethostbyname(tgthost)
        except Exception as e:
            print(str(e))
            exit(0)
        s.connect((g,tgtport))
        print("connection succesful ")
    except Exception as e:
        print(str(e))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-H','--host',dest='host',action='store',help='specify target host  ip or name')
    parser.add_argument('-p','--port',dest='port',action='store',help='specify target port')
    args=parser.parse_args()
    tgthost=args.host
    tgtports=str(args.port).split(',')
    for tgtport in tgtports :
        con(tgthost,tgtport)

if __name__=='__main__':
    main()
