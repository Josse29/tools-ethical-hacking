import socket 

# targetMachine = 192.168.107.97 // vulnerable machine 
 
def scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress,port))
        serviceversion = sock.recv(1024)
        print(f"Port {port} is open | " + str(serviceversion))
    except ConnectionRefusedError:
        print(f"Port {port} is closed")
target = input("Target : ")
ports = input("Port : ")

if ',' in ports :
    portlist = ports.split(',')
    for port in portlist:
        scan(target, int(port.strip()))
elif '-' in ports:
    portrange = ports.split('-')
    start = int(portrange[0])
    end = int(portrange[1])
    for port in range(start, end + 1):
        scan(target, port)    
else:
    scan(target, int(ports.strip()))

# scan(target, int(ports.strip()))


