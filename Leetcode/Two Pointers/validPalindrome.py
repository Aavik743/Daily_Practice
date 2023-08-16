def isPalindrome(s):
    output=''
    for element in s:
        if element.isalnum():
            output += element
    if output.lower() == output[::-1].lower():
        return True
    else:
        return False



# streeng = "A man, a plan, a canal: Panama"
streeng = "race a car"
print(isPalindrome(streeng))