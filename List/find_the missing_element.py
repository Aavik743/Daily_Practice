def find_the_missing_element(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    result = l1-l2
    return list(result)
    

l1 = [9,8,7,6,5,4,3,2,1]
l2 = [9,8,7,5,4,3,2,1]
print(find_the_missing_element(l1, l2))
