#Rearrange the array to maximun minimum from 
def rearrage(arr,n):
    temp=n*[None] #Creating an auxilary array
    small,large=0,n-1
    flag=True
    for i in range(n):
        if flag is True:
            temp[i]=arr[large]
            large -=1
        else:
            temp[i]=arr[small]
            small +=1
        flag=bool(1-flag)
    for i in range(n):#copy the temp array to main array
        arr[i]=temp[i]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(rearrage(arr,n))