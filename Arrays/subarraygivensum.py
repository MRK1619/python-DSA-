def subarray(a,n,sum):
    for i in range(n):
        cur_sum=a[i]
        j=i+1
        while(j<=n):
            if cur_sum==sum:
                print('index %d and %d' % (i,j-1))
                
                return 1
            if cur_sum>sum or j==n:
                break
            cur_sum=cur_sum+a[j]
            j+=1
    print('no subarray found')
    return 0
a=list(map(int,input().split()))
n=len(a)
sum=int(input())
subarray(a,n,sum)