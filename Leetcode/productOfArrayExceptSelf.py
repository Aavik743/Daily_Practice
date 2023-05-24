
def productOfArrayExceptSelf1(nums):
    output_arr = []
    mul = 1
    for num in nums:
        mul = mul * num
    for i in range(0,len(nums)):
        output_arr.append(mul//nums[i])
    return output_arr

def productOfArrayExceptSelf2(nums):
    # Create a result list with the same length as the input list and fill it with 1s.
    res = [1] * (len(nums))

    # Calculate the product of all numbers to the left of each element.
    # Initialize a variable called "prefix" to 1.
    prefix = 1
    for i in range(len(nums)):
        # Store the product of all numbers to the left of the current element in the result list.
        res[i] = prefix
        # Update the "prefix" by multiplying it with the current element.
        prefix *= nums[i]
    # Calculate the product of all numbers to the right of each element.
    # Initialize a variable called "postfix" to 1.
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        # Multiply each element in the result list by the product of all numbers to the right of it.
        res[i] *= postfix
        # Update the "postfix" by multiplying it with the current element.
        postfix *= nums[i]

    # Return the final result list.
    return res

def productOfArrayExceptSelf3(nums):
    output_arr = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        output_arr[i] = pre
        pre = pre * nums[i]
    post = 1
    for i in range(len(nums)-1,-1,-1):
        output_arr[i] = output_arr[i] * post
        post = post * nums[i]
    return output_arr
    



        

nums = [1,2,3,4]
print(productOfArrayExceptSelf3(nums))
# Output: [24,12,8,6] pre = [1,2,]