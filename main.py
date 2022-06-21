import socket
ip=input("Ip pls")
hostname=socket.gethostbyaddr(ip)
print(hostname)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target=hostname

print("start")

def port_scan(port):
    try:
        s.connect((ip, port))
        return True
    except:
        return False
port=0
while port<10:
    if port_scan(port):
        print('Port', port, 'is open')
        port += 1
    else:
        print("port", port, "is closed")
        port += 1
