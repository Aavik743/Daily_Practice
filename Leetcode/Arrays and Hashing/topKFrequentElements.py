# def topKFrequent(nums, k):
#     count = {}
#     freq = [[] for i in range(len(nums) + 1)]

#     for n in nums:
#         count[n] = 1 + count.get(n,0)
#     for n, c in count.items():
#         freq[c].append(n)

#     res = []
#     for i in range(len(freq) - 1, 0, -1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res) == k:
#                 return res

def topKFrequent(nums, k):
    # We have a list of numbers called "nums" and we want to find the top k most frequent numbers in the list.

    # We start by creating an empty dictionary called "count" to keep track of how many times each number appears in the list.
    count = {}

    # We also create an empty list called "freq" which will hold lists of numbers based on their frequency.
    # Each index of the "freq" list corresponds to a certain frequency value.
    # For example, if a number appears twice, it will be stored at index 2 of the "freq" list.
    freq = [[] for i in range(len(nums) + 1)]

    # We loop through each number in the "nums" list.
    for n in nums:
        # If the number is already in the "count" dictionary, we increase its count by 1.
        # Otherwise, if it's a new number, we set its count to 1.
        count[n] = 1 + count.get(n, 0)

    # After counting the frequency of each number, we iterate through the "count" dictionary.
    # We retrieve each number (n) and its corresponding count (c).
    for n, c in count.items():
        # We append the number (n) to the list at the index corresponding to its count (c) in the "freq" list.
        # This means that all numbers with the same count are grouped together.
        freq[c].append(n)

    # We create an empty list called "res" which will hold our final result.
    res = []

    # We iterate through the "freq" list in reverse order, starting from the highest frequency.
    # This allows us to find the most frequent numbers first.
    for i in range(len(freq) - 1, 0, -1):
        # For each frequency, we iterate through the list of numbers at that frequency.
        for n in freq[i]:
            # We add the number to the "res" list.
            res.append(n)
            # If we have collected enough numbers to make up the top k frequent numbers, we stop and return the result.
            if len(res) == k:
                return res

    # If we reach this point, it means that the top k numbers were not found in the "freq" list.
    # This could happen if the list "nums" had fewer than k unique numbers.
    # In that case, we simply return the numbers we have found so far in the "res" list.


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
# Output: [1,2]



