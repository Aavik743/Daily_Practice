"""
This is simple Program to reverse a given string
"""


def to_reverse_given_string(str2):
    str3 = str2[::-1]
    return str3


if __name__ == '__main__':
    str1 = "hello world"
    result = to_reverse_given_string(str1)
    print("The original string is", str1)
    print("The reversed string is", result)
