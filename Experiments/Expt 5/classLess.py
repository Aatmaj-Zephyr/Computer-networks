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


  
ip=input("Please enter ip: ")
subnetMask=input("Please enter subnetmask: ")
ip="".join([toBinary(i) for i in ip.split(".")])
print(ip)
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


 
