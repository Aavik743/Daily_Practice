"""
    This is a Program to take a list and pair two consecutive elements and add them
"""


def add_pair_num(a):
    b = []
    for i in range(0, len(a), 2):
        if i + 1 < len(a):
            output = a[i] + a[i + 1]
        else:
            output = a[i]
            i += 1
        b.append(output)
    return b


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("The given list is", a)
    pair_sum = add_pair_num(a)
    print("The result is", pair_sum)
