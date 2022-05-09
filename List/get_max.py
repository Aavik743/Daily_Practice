def find_max_num(list):
    result_list = []
    for i in range(len(list) - 2):
        one = i
        two = i + 1
        three = i + 2
        num = max_of_three(list[one], list[two], list[three])
        result_list.append(num)
        one += 1
        two += 1
        three += 1
    return result_list


def max_of_three(first, second, third):
    if first > second and first > third:
        return first
    if second > first and second > third:
        return second
    if third > first and third > second:
        return third


if __name__ == '__main__':
    input_list = [10, 5, 2, 7, 8, 7]
    result = find_max_num(input_list)
    print(result)
