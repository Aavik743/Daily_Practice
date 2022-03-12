def sum_(list1, list2):
    sum_list = []
    for i in range(3):
        sum_list.append(list1[i] + list2[i])
    return sum_list


if __name__ == '__main__':
    list_1 = [1, 2]
    list_2 = [2, 4]
    sum(list_1, list_2)
