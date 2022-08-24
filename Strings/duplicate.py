def duplicate(str):
    s=set()
    for i in str:
        s.add(i)
    st= ""
    for i in s:
        st=st+i
    return st
str=input()
print(duplicate(str))
