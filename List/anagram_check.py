
def anagram_check1(str1, str2):
    str1=sorted(str1.replace(" ", "").lower())
    str2=sorted(str2.replace(" ", "").lower())
    if str1 == str2:
        return True
    else:
        return False
        
def anagram_check2(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    count = {}
    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False
        else:
            return True
               
if __name__ == '__main__':
    inp1 = "dog"
    inp2 = "God"
    print(anagram_check2(inp1, inp2))