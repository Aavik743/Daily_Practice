"""An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they
exists). Given an array arr[] of size N, find the index of any one of its peak elements. """


# function should return index to the any valid peak element
def peakElement(arr, n):
    if n == 1:
        return 0
    for i in range(n):
        if i == 0:
            if arr[i] > arr[i + 1]:
                return i
        if i == (n - 1):
            if arr[i] > arr[i - 1]:
                return i
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            return i


#  Driver Code Starts
if __name__ == '__main__':
    arr = [1, 2, 3]
    n = len(arr)
    print(peakElement(arr, n))
