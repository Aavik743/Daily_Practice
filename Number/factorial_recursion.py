def get_factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)


if __name__ == '__main__':
    input_num = 4
    fact = get_factorial(input_num)
    print('The factorial of', input_num, ' is', fact)
