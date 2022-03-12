a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
for i in range(0, len(a), 2):
    if i + 1 < len(a):
        output = a[i] + a[i + 1]
    else:
        output = a[i]
        i += 1
    b.append(output)
print(b)
