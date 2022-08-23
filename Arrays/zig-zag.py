#zig zag formation
def zig_zag(arr,size):
    flag=True
    for i in range(size-1):
        if flag is True:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        flag=bool(1-flag)
    print(arr)
    
arr=list(map(int,input().split()))
size=len(arr)
zig_zag(arr,size)
                