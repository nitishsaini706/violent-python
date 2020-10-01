
import argparse
from socket import *
import os 

def conscan(tgthost,tgtport):
    try:
        setdefaulttimeout(2)
        connskt=socket(AF_INET,SOCK_STREAM)
        connskt.connect((tgthost,int(tgtport)))
        print ("tcp port :  "+ tgtport+ " is open ")
    except Exception as e:
        print(str(e))
    finally:
        connskt.close()
def portscan(tgthost,tgtports):
    try:
        tgtip=gethostbyname(tgthost)
    except:
        print("cannot resolve "+tgthost)
    try:
        tgtname=gethostbyaddr(tgtip)
        print("scan results for :"+ tgtname[0])
    except:
        print ("scan result for : "+tgtip)
    setdefaulttimeout(2)
    for tgtport in tgtports:
        print("scanning for : " + tgtport)
        conscan(tgthost,tgtport)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-H','--host',dest='host',action='store' ,help='specify target host')
    parser.add_argument('-p','--ports',dest='ports',action='store',help='specify tareget port')
    args=parser.parse_args()
    tgthost=args.host
    tgtports=str(args.ports).split(',')
    if tgthost==None or tgtports==None:
        print('specify target hosts and port')
        exit(0)
    portscan(tgthost,tgtports)
if __name__=='__main__':
    main()
