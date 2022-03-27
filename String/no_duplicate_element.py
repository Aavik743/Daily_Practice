def remove_duplicates(str):
    result = ""
    comma = ","
    for element in str:
        if element not in result:
            if element == " ":
                continue
            else:
                 result = result + element + comma
    print(result)


if __name__ == '__main__':
    input_str = 'hello world'
    remove_duplicates(input_str)

