def to_check_palindrome(string):
    new_string = string[:: -1]

    if new_string == string:
        print('The string-->', string, 'is a palindrome')
    else:
        print('The string-->', string, 'is not a palindrome')


if __name__ == '__main__':
    str_1 = "hello"
    str_2 = "asdfdsa"
    to_check_palindrome(str_1)
    to_check_palindrome(str_2)
