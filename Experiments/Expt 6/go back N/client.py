# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345			
recieved = []

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
frame = 0
while True:
    # receive data from the server and decoding to get the string.

    val = s.recv(1024).decode()
    print(val)
    val = int(val)
    recieved.append(val)
    if(frame == val):
        print ("recieved")
        frame = frame +1
        frame = frame % 7
        s.send(str(val).encode()) # ack
    else: 
        s.send("-1".encode()) # nack
# close the connection 

s.close()	 
	
