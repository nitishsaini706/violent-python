from winreg import *

def Nets():
    net="\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    print(net)
    key=OpenKey(HKEY_LOCAL_MACHINE,net)
    print('network joined')
    for i in range(100):
        try:
            guid=EnumKey(key,i)
            netkey=OpenKey(key,str(guid))
            (n,addr,t)=EnumValue(netkey,5)
            (n,name,t)=EnumValue(netkey,4)
            macAddr=val2addr(addr)
            Netname=str(name)
            print(Netname+' '+macAddr)
            closeKey(netkey)
        except:
            break

def val2addr(val):
    addr=" "
    for ch in val:
        addr+= ( " %02x " % ord(ch))
        addr=addr.strip(" ").replace(" ",":")[0:17]
        return addr

def main():
    print (Nets())

if __name__=='__main__':
    main()