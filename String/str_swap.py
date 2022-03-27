def swap_str(str):
    str = list(str)
    first = 0
    last = len(str) - 1
    for i in range(0, len(str)//2):
        str[first], str[last] = str[last], str[first]
        first += 1
        last -= 1
    print(str)


if __name__ == '__main__':
    input_string = '123456'
    swap_str(input_string)
