def check_common_char(str1, str2):
    list_ = []
    common_chars = set(str1) & set(str2)
    list_.append(common_chars)
    print(list_)


if __name__ == '__main__':
    str_a = "hello"
    str_b = "world"
    check_common_char(str_a, str_b)
