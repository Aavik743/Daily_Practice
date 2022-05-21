def do_intersection(a, b):
    res = []
    if len(a) > len(b):
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    res.append(a[i])
    if len(b) > len(a):
        for i in range(len(b)):
            for j in range(len(a)):
                if b[i] == a[j]:
                    res.append(b[i])
    for i in range(0, len(res)):
        print(res[i], end=' ')


if __name__ == '__main__':
    arr_a = [1, 2, 3, 4, 5]
    arr_b = [1, 2, 3]
    do_intersection(arr_a, arr_b)
