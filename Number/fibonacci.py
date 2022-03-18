def findFibonacci(n):
    list_ = []
    for i in range(0, n + 1):
        list_.append(i)

    for i in range(0, len(list_) + 1):
        print(list_[i] + list_[i + 1])


if __name__ == '__main__':
    k = int(input("Enter the nth positive number of the fib series: \n"))
    findFibonacci(k)
