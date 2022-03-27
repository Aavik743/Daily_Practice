def add_matrices(x, y):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(0, len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
            # result.append(add)
    print(result)


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
    ]

    add_matrices(a, b)
