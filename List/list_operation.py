list_1 = [1, 2, 3, 4]
list_2 = []
first = 0
last = len(list_1) - 1
while first <= last:
    list_2.append(list_1[first])
    first += 1
    list_2.append(list_1[last])
    last -= 1
print(list_2)
