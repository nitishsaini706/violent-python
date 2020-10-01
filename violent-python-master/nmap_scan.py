#!/usr/lib/python3.8

import nmap 
import argparse 

def nmapscan(tgthost,tgtport):
    nmscan=nmap.PortScanner()
    nmscan.scan(tgthost,tgtport)
    try:
       state=nmscan[tgthost]['tcp'][int(tgtport)]['state']
       if state=='open':
             print("[*]"+tgthost+" tcp "+tgtport+"   "+state)
       else:
           print("port "+tgtport+" closed")
    except Exception as e:
        print("error occured as " +str(e))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-H",'--host',action='store',dest='tgthost',help='specify tareget host ip')
    parser.add_argument('-p','--port',action='store',dest='tgtport',help='specify target port number')
    args=parser.parse_args()
    tgthost=args.tgthost
    tgtport=args.tgtport
    if not tgthost or tgtport:
        print('[-]specfiy port and host ')
        exit(0)
    else:
         print("scanning hsa begun")
         nmapscan(tgthost,tgtport)

if __name__=='__main__':
    main()