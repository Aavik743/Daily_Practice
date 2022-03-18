def get_sum(list_):
    even = 0
    odd = 0

    for i in range(0, len(list_)):
        if list_[i] % 2 == 0:
            even = list_[i] + even
        else:
            odd = list_[i] + odd
    print('Sum of even numbers-->', even)
    print('Sum of even numbers-->', odd)


if __name__ == '__main__':
    list_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    get_sum(list_input)
