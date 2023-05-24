# def encodeAndDecodeStrings(inp):
#     if type(inp) == list:
#         output = ""
#         for i in range(len(inp)-1):
#             output += inp[i] + "#"
#         output += inp[len(inp)-1]+"$"
#     else:
#         output = inp[:-1].split("#")
#     return output

def encodeAndDecodeStrings(inp):
    if isinstance(inp, list):
        return '#'.join(inp) + '$'
    else:
        return inp[:-1].split('#')
    

input1 = ["encode", "and", "decode", "strings"]

# Output:"encode#and#decode#strings$"

input2 = "encode#and#decode#strings$"

# Output:["encode", "and", "decode", "strings"]

print(encodeAndDecodeStrings(input1))