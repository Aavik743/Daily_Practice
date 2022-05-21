def segregate_elements(arr, n):
    # Your code goes here
    neg = []
    pos = []

    for i in range(n):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    res = pos + neg
    for i in range(0, len(res)):
        print(res[i], end=' ')


if __name__ == '__main__':
    n = 8
    arr = [1, -1, 3, 2, -7, -5, 11, 6]
    segregate_elements(arr, n)
