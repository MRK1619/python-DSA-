#find a middle number where left sum equal right sum
def equilibram(arr,size):
    i,start,end,left_sum,right_sum=0,0,size-1,0,0
    for i in range(size):
        if(start== end and right_sum==left_sum):
            return arr[start]
        if(start==end):
            return -1
        if(left_sum>right_sum):
            right_sum +=arr[end]
            end -= 1
        elif(left_sum<right_sum):
            left_sum +=arr[start]
            start += 1
        else:
            right_sum +=arr[end]
            end -= 1
    if (not i):
        return arr[0]
arr=list(map(int,input().split()))
size=len(arr)
print(equilibram(arr,size))