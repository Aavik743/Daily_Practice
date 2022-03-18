def check_perfect(num):
    sum = 1
    for i in range(2, num // 2 + 1):
        if (num % i) == 0:
            sum = sum + i

    if sum == num:
        print(num, ' is a perfect number')
    else:
        print(num, ' is a not perfect number')
    return


if __name__ == '__main__':
    n = 6
    check_perfect(n)
