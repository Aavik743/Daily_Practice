def twoSum(nums, target):
    nums_enum = enumerate(nums)
    output = {}
    for k,v in nums_enum:
        check = target - v
        if check in output:
            output[v]=k
        else:
            print([min(output[check],k), max(output[check],k)])
for i, j in enumerate(num):
    if num[i] + num[i+1] == target:
        print([i, i+1])
        break
                
        
    
    
if __name__ == '__main__':
    nums = [3,2,4] 
    target = 6
    twoSum(nums, target)