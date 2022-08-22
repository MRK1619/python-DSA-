#sort as 0 1 2
def sort012(arr,size):
    low,mid,high=0,0,size-1
    while mid <= high:
        if arr[mid]== 0:
            arr[low], arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
        elif arr[mid]==1:
            mid=mid+1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1
    return arr

def printArry(arr):
    for k in arr:
        print(k, end=' ')
        
arr=list(map(int,input().split()))
size=len(arr)
arr=sort012(arr,size)
printArry(arr)