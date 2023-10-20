def toBinary(a):
    a=int(a)
    answer=[]
    if(a==0):
        return 0
    while(a!=0):
        answer.append(str(a%2))
        a=a//2

    while(len(answer)<8):
        answer.append('0')
    return("".join(answer[::-1]))
def toDecimal(a):
    a=str(a)
    answer=0
    power=0
    for digit in a[::-1]:
        if(digit=='1'):
            answer+=2**power
        power+=1
    return answer

def addBin(a):
    #print(a)
    a=[i for i in a]
    #print(a)
    a=a[::-1]
    #print(a)
    for i in range(len(a)):
        if(a[i]=='0'):
            a[i]='1'
            break
        else:
            a[i]='0'
    a=a[::-1]
    #print(a)
    a="".join(a)
    return a
ip=input("Please enter ip: ")
subnetMask=input("Please enter subnetmask: ")
subnets = input("please enter number of subnets: ")

def subnet(ip,subnetMask):
    ip="".join([toBinary(i) for i in ip.split(".")])
    #print(ip)
    subnetMask = "".join(['1' if i<int(subnetMask) else '0' for i in range(32)])

    first = ['1' if(int(ip[i])*int(subnetMask[i])==1) else '0' for i in range(0,len(ip))]
    first=["".join(first[i:i + 8]) for i in range(0, len(first), 8)] # split in 4 parts of 8
    first=".".join([str(toDecimal(i)) for i in first])

    print(first) #network ip

    subnetMask = ['0' if i=='1' else '1' for i in subnetMask]

    last = ['0' if(int(ip[i])+int(subnetMask[i])==0) else '1' for i in range(0,len(ip))]
    last=["".join(last[i:i + 8]) for i in range(0, len(last), 8)] # split in 4 parts of 8
    last=".".join([str(toDecimal(i)) for i in last])

    print(last) #network ip
    return last
"""
ip="123.23.24.2"
subnetMask = "23" 
subnets="3"
"""

subnets = int(subnets)
import math
for k in range((int(subnets))):
    print("subnet number ",k)
    ip = subnet(ip,int(subnetMask)+math.ceil(math.log(subnets)/math.log(2)))

    ip= ip.split(".")
    #print(ip)
    ip = "".join([toBinary(i) for i in ip])
    #print(ip)
    ip= addBin(ip)
    #print(ip)
    ip=["".join(ip[i:i + 8]) for i in range(0, len(ip), 8)] # split in 4 parts of 8
    #print(ip)
    ip=[str(toDecimal(i)) for i in ip]
    ip=".".join(ip)
    #print(ip)