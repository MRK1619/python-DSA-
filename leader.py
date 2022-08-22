#leaders from last to fast
def leader(arr, size):
    max_from_left = arr[size-1]
    print(max_from_left, end=' ')
    for i in range(size-2, -1, -1):
     if max_from_left < arr[i]:
        print(arr[i], end=' ')
        max_from_left = arr[i]
arr=list(map(int, input().split()))
size=len(arr)
leader(arr,size)
    
    



