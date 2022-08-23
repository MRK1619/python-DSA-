#reverse in a given range
def reverse(arr,size,k):
    i=0
    while(i<size):
        left=i
        right=min(i+k-1,size-1)
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left +=1
            right -=1
        i+=k
        
arr=list(map(int,input().split()))
size=len(arr)
k=3
reverse(arr,size,k)
for i in range(0, size):
    print(arr[i], end=' ')
    
    