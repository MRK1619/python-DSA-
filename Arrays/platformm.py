#nalve approch
def findPaltform(arr,dep,n):
    plat_need=1
    result=1
    for i in range(n):
        plat_need=1
        for j in range(i+1,n):
            if(max(arr[i],arr[j])<=min(dep[i],dep[j])):
                plat_need+=1
        result=max(result,plat_need)
    return result

arr=list(map(int,input().split()))
dep=list(map(int,input().split()))
n=len(arr)
print(findPaltform(arr,dep,n))