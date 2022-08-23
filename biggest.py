#from the biggest number from the array
from itertools import permutations
def biggest(arr):
    big=[]
    for i in permutations(arr,len(arr)):
        big.append("".join(map(str,i)))
    return max(big)
arr=list(map(int,input().split()))
print(biggest(arr))
    