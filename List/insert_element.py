def to_insert_element(list1, k):
    index = len(list1)
    for i in range(len(list1)):
        if list1[i] > k:
            index = i
            break
    if index == len(list1):
        list1 = list1(index) + [k]
    else:
        list1 = list1[:index] + [k] + list1[index:]
    print(list1)


if __name__ == '__main__':
    list_1 = [1, 3, 5, 7, 10]   # list provided
    k = 6   # element to be inserted
    to_insert_element(list_1, k)
