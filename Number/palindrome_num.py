def palindrome_checker(num):
    temp = num
    rev_num = 0
    while temp != 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp = temp // 10
    if num == rev_num:
        print('palindrome')
    else:
        print('not palindrome')


if __name__ == '__main__':
    in_num = 1234321
    palindrome_checker(in_num)
