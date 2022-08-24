#reverse the string
def reverse(str,l):
    if l%2==0:
        j=int(l/2)
        while(j<=l-1):
            str[j],str[l-j-1]=str[l-j-1],str[j]
            j+=1
    else:
        j=int(l/2+1)
        while(j<=l-1):
            str[j],str[l-j-1]=str[l-j-1],str[j]
            j+=1
        return str
str=input()
string=str.split(' ')
string=reverse(string,len(string))
print(" ".join(string))            
            
            
    