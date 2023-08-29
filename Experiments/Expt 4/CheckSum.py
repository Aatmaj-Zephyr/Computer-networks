def toDecimal(a):
    a=str(a)
    answer=0
    power=0
    for digit in a[::-1]:
        if(digit=='1'):
            answer+=2**power
        power+=1
    return answer

def toBinary(a):
    a=int(a)
    answer=[]
    if(a==0):
        return 0
    while(a!=0):
        answer.append(str(a%2))
        a=a//2
    return("".join(answer[::-1]))
    
    
data=['110','101','001','000']

def checkSumCalculate(data):
    checkSum=toBinary(sum([toDecimal(int(i)) for i in data])) #110+101+001+000 = 1100
    
    if(len(checkSum)>len(data[1])):
        #wrap carry
        checkSum=toBinary(toDecimal(checkSum)+1)
        checkSum = str(checkSum) # necesary to convert to string
        checkSum=checkSum[1::] # remove first digit
        #101
    #complement checkSum
    checkSum = str(checkSum) # necesary to convert to string
    checkSum="".join(['1' if i=='0' else '0' for i in checkSum]) #010
    return checkSum

sent = data+[checkSumCalculate(data)]
print("data sent is",sent)

recieved = sent

validate = True if checkSumCalculate(recieved)=='000' else False
print(validate)
