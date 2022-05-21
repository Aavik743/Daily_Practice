def get_fibonacci(n):
    list_ = []
    for i in range(0, n + 1):
        list_.append(i)

    index = 0
    res = 0
    while index < len(list_):
        res += list_[index]
        print(res, end=' ')
        index += 1


if __name__ == '__main__':
    k = int(input("Enter the nth positive number of the fib series: \n"))
    get_fibonacci(k)
