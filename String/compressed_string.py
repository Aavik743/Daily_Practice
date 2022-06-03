# input = aabbcc
# using for loop
def comp_string_1(s):
    n = len(s)
    count = 1
    new_str = ''
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            new_str = new_str + s[i] + str(count)
            count = 1
    new_str = new_str + s[n-1] + str(count)
    return new_str


if __name__ == '__main__':
    in_string = 'aabbbcc'
    print(comp_string_1(in_string))
