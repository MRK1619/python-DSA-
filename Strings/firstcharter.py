#first repeted array
def repeat(str):
    h={} #create a empty hash
    for ch in str:
       if ch in h:
           return ch
       else:
           h[ch]=0
    return ''
str=input()
print(repeat(str))
    