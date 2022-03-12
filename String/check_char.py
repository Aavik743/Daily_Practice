def char_count(str):
    dict1 = {}
    for _char in str:
        if _char in dict1:
            dict1[_char] += 1
        else:
            dict1[_char] = 1
    return dict1


if __name__ == '__main__':
    str_in = 'hello How  are you, doing well?'
    counter = char_count(str_in)
    print(counter)