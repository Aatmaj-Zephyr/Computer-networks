generator='1001'
code='11100101'

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
    
sent=str(code+str(toBinary(toDecimal(code)%toDecimal(generator))))

print("Sent data is ",sent)
print()
recieved = sent

isCorrect = True if toBinary(toDecimal(recieved)%toDecimal(generator)) ==0 else False
print("Data recieved correctly?", isCorrect)
