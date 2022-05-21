""" Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array. """


def getMinMax(a, n):
    a.sort()
    return [a[0], a[n - 1]]


# Driver Code Ends
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    n = len(a)
    print(getMinMax(a, n))
