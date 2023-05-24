# This function finds the length of the longest consecutive sequence of numbers in a given list of numbers.

def longestConsecutive(nums):
    # First, we convert the list of numbers into a set.
    # A set is like a collection of unique items, so any duplicate numbers are removed.
    nums_set = set(nums)

    # We initialize a variable called "streak" to keep track of the longest consecutive sequence found so far.
    streak = 0

    # Now, we loop through each number in the list.
    for num in nums:
        # We check if the current number minus 1 (one less than the current number) is not present in the set.
        # If it's not in the set, it means the current number is the start of a new consecutive sequence.
        if num-1 not in nums_set:
            # If it is the start of a new sequence, we initialize a variable called "count" to 1.
            # This variable will keep track of the length of the current consecutive sequence.
            count = 1

            # We enter a while loop that continues as long as the next number in the consecutive sequence is present in the set.
            while num+count in nums_set:
                # Inside the loop, we increment the count by 1 to move to the next number in the sequence.
                count += 1

            # After the while loop finishes, we compare the length of the current sequence (count) with the longest sequence found so far (streak),
            # and update the streak if the current sequence is longer.
            streak = max(streak, count)

    # Finally, we return the length of the longest consecutive sequence.
    return count


# Example usage:
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
