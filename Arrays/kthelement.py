#kth ememrnt from 2 sorted array
def kth(a,b,m,n,k):
    pq=[]; #declaring a min heap
    for i in range(m):
        pq.append(a[i])
    for i in range(n):
        pq.append(b[i])
    pq=sorted(pq,reverse=True)
    
    while(k>1):
        k-=1;
        pq.pop();
    return pq.pop();
a=list(map(int,input().split())) 
b=list(map(int,input().split()))
m=len(a)
n=len(b)
k=int(input())
print(kth(a,b,m,n,k))