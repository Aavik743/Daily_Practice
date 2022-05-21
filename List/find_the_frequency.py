"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""


def find_frequency(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count


if __name__ == '__main__':
    N = 5
    input_list = [1, 1, 1, 1, 1]
    X = 1
    print(find_frequency(input_list, N, X))
