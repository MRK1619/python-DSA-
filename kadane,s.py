#maxSubarraySum
def maxSubarraySum(a,n):
    max=a[0]
    max_ending=0
    for i in range(0,n):
        max_ending=max_ending+a[i]
        if(max_ending>max):
            max=max_ending
        if max_ending<0:
            max_ending=0
    return max

a=list(map(int,input().split()))
n=len(a)
print(maxSubarraySum(a,n))
