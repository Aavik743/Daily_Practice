def get_count(str):
    vowel_count = 0
    conso_count = 0
    str = str.replace(" ", '')
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for char in str:
        if char.lower() in vowel_list:
            vowel_count += 1
        else:
            conso_count += 1
    return vowel_count, conso_count


if __name__ == '__main__':
    input_string = 'hello world'
    vowels, consonants = get_count(input_string)
    print('The number of vowels are', vowels)
    print('The number of consonants are', consonants)
