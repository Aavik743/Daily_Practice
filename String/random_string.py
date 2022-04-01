import random


def generate_random_strings(str):
    temp_str = None
    string_count = 0
    while str != temp_str:
        temp_str = ''.join((random.choice(str)) for i in range(len(str)))
        string_count += 1
    return string_count


if __name__ == '__main__':
    input_string = 'hello'
    count = generate_random_strings(input_string)
    print('No. of random strings generated is', count)
