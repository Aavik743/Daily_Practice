def find_hcf(num1, num2):
    list1 = []
    list2 = []
    list_ = []

    for i in range(2, num1 // 2 + 1):
        if (num1 % i) == 0:
            num1 = (num1 // 2)
            list1.append(i)

    for j in range(2, num2 // 2 + 1):
        if (num2 % j) == 0:
            num2 = (num2 // 2)
            list2.append(j)

    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                list_.append(list1[i])

    print(list_)


if __name__ == '__main__':
    num_a = 10
    num_b = 12
    find_hcf(num_a, num_b)
