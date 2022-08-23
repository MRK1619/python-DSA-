#buy stocks and sell stocks
def stockbuy(arr,n):
    if(n==1):
        return
    i=0
    while(i<(n-1)):
        while((i<(n-1)) and (arr[i+1]<=arr[i])):
            i+=1
        if (i==n-1):
            break
        buy=i
        i+=1
        while((i<n) and (arr[i]>=arr[i-1])):
            i+=1
        sell=i-1
        print('Buy on day:',buy, "\t",'sell on day:' ,sell)
arr=list(map(int,input().split()))
n=len(arr)
stockbuy(arr,n)