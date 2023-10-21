# first of all import the socket library 
import socket			 

# next create a socket object 
s = socket.socket()		 
print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345			

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 

# put the socket into listening mode 
s.listen(5)	 
print ("socket is listening")		 

# a forever loop until we interrupt it or 
# an error occurs 

while True: 
    #sliding window of 7 


    # Establish connection with client. 
    c, addr = s.accept()	 
    print ('Got connection from', addr )
    recieved = [0,1,2,3,4,5,6,7] # sliding window
    counter = 0
    time = 0
    for i in range(100):
        print("time = ", time)
        print("counter = ", counter)
        time +=1
        if(time % 7 > counter + 6):
            time = counter # go back
            print("going back")
        c.send(str(time % 7).encode())  #send to client
        
        val = int(c.recv(1024).decode())
        if(val>=counter):
            counter = val +1
            counter = counter % 7
            # proceed
        print("val = ", val)
        

    # Close the connection with the client 
    c.close()

    # Breaking once connection closed
    break
