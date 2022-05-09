def get_even_words(str):
    even_words = []
    words = str.split()
    for i in range(0, len(words) - 1):
        if len(words[i]) % 2 == 0:
            even_words.append(words[i])
    print(even_words)


if __name__ == '__main__':
    input_string = 'this program is written on pycharm only'
    get_even_words(input_string)
