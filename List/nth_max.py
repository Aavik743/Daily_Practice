def find_max(list_, k):
        n = len(list_)
        print(list_[n - k])


if __name__ == '__main__':
    list_1 = [3, 5, 4, 1, 0, 2]
    list_ = sorted(list_1)
    k = int(input("Enter the k-th largest element: \n"))
    find_max(list_, k)