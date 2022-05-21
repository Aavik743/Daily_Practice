# Function to return the count of number of elements in union of two arrays.
def doUnion(a, b):
    # code here
    res = set(a + b)
    return len(res)


if __name__ == '__main__':
    arr_a = [1, 2, 3, 4, 5]
    arr_b = [1, 2, 3]
    print(doUnion(arr_a, arr_b))
