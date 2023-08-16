def isAnagram(a, b):
    if len(a) != len(b):
        return False
    a = "".join(sorted(a))
    b = "".join(sorted(b))
    if a == b:
        return True
    else:
        return False
    

# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
print(isAnagram(s,t))