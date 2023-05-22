# def groupAnagrams(strs):
#     strs_output = []
#     for streeng in strs:
#         # breakpoint()
#         sorted_streeng = "".join(sorted(streeng))
#         found = False
#         for sub_list_index in range(len(strs_output)):
#             if "".join(sorted(strs_output[sub_list_index][0])) == sorted_streeng:
#                 strs_output[sub_list_index].insert(0, streeng)
#                 strs_output[sub_list_index].sort()
#                 found = True
#                 break
#         if not found:
#             strs_output.insert(0, [streeng])
#     return strs_output
def groupAnagrams(strs):
    output_dict = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in output_dict:
            output_dict[key].append(word)
        else:
            output_dict[key] = [word]
    output = list(output_dict.values())
    return output
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]

#pick a string...sort it..check if it exists in any of the sub lists..if not append it as a sub list