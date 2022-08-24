def anagram(a,b):
    if sorted(a)==sorted(b):
        print("Anagram")
    else:
        print("not anagram")
a=input()
b=input()
anagram(a,b)
