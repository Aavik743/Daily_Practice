decToHexDict = {0: '0', 1: '1', 2: '2', 3: '3',
                4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B',
                12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hexToDec(dec_num):
    hex = ''
    while dec_num > 0:
        rem = dec_num % 16
        hex = decToHexDict[rem] + hex
        dec_num = dec_num // 16
    return hex


if __name__ == '__main__':
    num = 31
    conversion = hexToDec(num)
    print('Decimal', num, 'is converted to', conversion)
