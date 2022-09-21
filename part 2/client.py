from time import perf_counter
from socket import *
    
# Create a UDP socket 
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Waits the message for 0.5 second
clientSocket.settimeout(0.5)

# Address of server which will be connceted
serverAddr = ('192.168.1.37', 12000)

# Ping messages sent 10 times
for i in range(10):
    
    before = perf_counter()
    message = "PingMessage" + str(i + 1)
    clientSocket.sendto(message.encode(), serverAddr)
    
    try:
        data, server = clientSocket.recvfrom(1024)
        after = perf_counter()
        rtt = after - before
        print("Message Received: ", message, ", Round Trip Time in Seconds: ", rtt, sep="")
    
    except timeout:
        print("Request Times Out.")
