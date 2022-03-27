"""
    This is a simple Program to add elements of two lists of same length
"""


def sum_(list1, list2):
    sum_list = []
    for i in range(0, len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list


if __name__ == '__main__':
    list_1 = [1, 2]
    print("The first list is", list_1)
    list_2 = [2, 4]
    print("The first list is", list_2)
    output = sum_(list_1, list_2)
    print("The sum of the elements in the lists are", output)
