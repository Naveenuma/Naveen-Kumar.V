n = int(input())
count=0
num=101
while count<n:
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    if prime:
        if count>0:
            print(",",end="")
        print(num,end="")
        count+=1
    num+=1 
    
