def array_pair_sum1(inp_arr, target_sum):
    pair_list = []
    for num1 in inp_arr:
        for num2 in inp_arr:
            if num1 + num2 == target_sum:
                pair = sorted((num1, num2))
                if pair not in pair_list:
                    pair_list.append(pair)
    return {"pair_list": pair_list, "count": len(pair_list)}

def array_pair_sum2(inp_arr, target_sum):
    if len(inp_arr) < 2:
        return
    seen = set()
    output = set()
    for num in inp_arr:
        target = target_sum - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num), max(target,num)))
    return len(output)

if __name__ == '__main__':
    inp_arr = [1, 3, 2, 2, 5, -1]
    target_sum = 4
    print(array_pair_sum2(inp_arr, target_sum))