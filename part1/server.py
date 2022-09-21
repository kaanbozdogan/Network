#import socket module
from socket import *                              
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
HOST = '0.0.0.0'
PORT = 8080

serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        #get message
        message = connectionSocket.recv(1024)
        
        filename = message.split()[1]
        f = open(filename[1:])

        #get contents of this file                     
        outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode('utf-8'))
        connectionSocket.send('Content-Type: text/html\r\n'.encode('utf-8'))
        connectionSocket.send('\r\n'.encode('utf-8'))

        #Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode('utf-8'))

        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode('utf-8'))

        #Close client socket
        connectionSocket.close()

serverSocket.close()