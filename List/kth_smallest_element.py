""" Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest
element in the given array. It is given that all array elements are distinct. """


def kth_smallest(arr, k):
    """
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    """
    if k < len(arr):
        arr.sort()
        return arr[k - 1]


if __name__ == '__main__':
    input_array = [6, 5, 3, 8, 9, 2]
    n = int(input("Enter the kth element: "))
    print(kth_smallest(input_array, n))
