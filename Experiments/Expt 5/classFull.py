#classfull
ip=input("Please enter ip: ")
first=int(ip.split(".")[0])
if(first in range(0,127)):
    print("Class A")
    print("subnet mask: 255.0.0.0")
elif(first in range(128,191)):
    print("Class B")
    print("subnet mask: 255.255.0.0")
elif(first in range(192,223)):
    print("Class C")
    print("subnet mask: 255.255.255.0")
elif(first in range(224,239)):
    print("Class D")
    print("subnet mask: - ")
elif(first in range(240,256)):
    print("Class E")
    print("subnet mask: - ")
    
print("First address is ", first,".0.0.1")
print("Last address is ",first,".255.255.255")
