def getSums(list_):
    pos = 0
    neg = 0
    for num in list_:
        num = int(num)
        if num > 0:
            pos += list_(num)
        else:
            neg += list_(num)
    print("The sum of the positive numbers is", pos)
    print("The sum of the positive numbers is", neg)


if __name__ == '__main__':
    _list = [-1, 2, -3, 4, -5, 6, -7, 8]
    getSums(_list)
