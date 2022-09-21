from socket import * 

HOST = '127.0.0.1'
PORT = 8080

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((HOST, PORT))

soc.send("asd /asd.html".encode())

data = soc.recv(1024)
print(data.decode())

"""
data = soc.recv(1)
while data:
    print(data.decode(), end="")
    data = soc.recv(1)
"""