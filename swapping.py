#naive approch
def getsum(x):
    sum=0
    for i in x:
        sum+=i
    return sum
def findSwap(a,b):
    sum1=getsum(a)
    sum2=getsum(b)
    
    k=False
    val1=0
    val2=0
    for i in a:
        for j in b:
            newsum1=sum1-i+j
            newsum2=sum2-j+i
            
            if newsum1==newsum2:
                val1=i
                val2=j
                k=True
                break
        if k==True:
            break
    print(val1,val2)
    return

a=list(map(int,input().split()))
b=list(map(int,input().split()))
findSwap(a,b)