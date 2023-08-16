# def maxArea(height):
#     count = 0
#     max_amount = 0
#     rev_height = height[::-1]
#     for num in height:
#         count += 1
#         if len(height[count:]) == num : 
#             amount = num**2
#             if amount > max_amount:
#                 max_amount = amount
#         if len(height[:count-1]) == num and rev_height[count] >= num:
#             amount = num**2
#             if amount > max_amount:
#                 max_amount = amount

#     return max_amount

# def maxArea(height_list):
#     max_area = 0

#     for i in range(len(height_list)-1):
#         for j in range(i+1,len(height_list)):
#             height = min(height_list[i], height_list[j])
#             distance = abs(i-j)
#             area = height * distance
#             if area > max_area:
#                 max_area = area
#     return max_area

def maxArea(height_list):
    max_area = 0

    left_ptr = 0
    right_ptr = len(height_list) - 1

    while left_ptr < right_ptr:
        max_area = max(max_area, min(height_list[left_ptr], height_list[right_ptr])*abs(left_ptr-right_ptr))
        if height_list[left_ptr] <= height_list[right_ptr]:
            left_ptr += 1
        else:
            right_ptr -= 1
    return max_area


height_array = [1,8,6,2,5,4,8,3,7]
print(maxArea(height_array))