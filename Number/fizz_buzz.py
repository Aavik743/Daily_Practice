# divisible by 3 - fizz
# divisible by 5 - buzz
# divisible by 15 - fizz buzz

def fizzbuzz(n):
    dict_ = {3: 'Fizz', 5: 'Buzz', 15: 'FizzBuzz'}
    if n % 3 == 0 and n % 5 == 0:
        print(dict_[15])
    elif n % 3 == 0:
        print(dict_[3])
    elif n % 5 == 0:
        print(dict_[5])


if __name__ == '__main__':
    input_num = 45
    fizzbuzz(input_num)
