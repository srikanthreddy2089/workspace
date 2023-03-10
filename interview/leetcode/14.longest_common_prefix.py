#https://leetcode.com/problems/longest-common-prefix/
"""
Find min len all items in list and iterate that many times. Pick each letter from first item of list.
Match it with all other words of same position. If not matched, return else append that letter.
"""
def longestCommonPrefix(strs):
    min_lenght = min(len(a) for a in strs)
    common_prefix = ""

    for pos in range(min_lenght):
        each_letter = strs[0][pos]
        for each_word in strs:
            if each_word[pos] != each_letter:
                return common_prefix
        common_prefix += each_letter
    return common_prefix

strs = ["flower","flow","floght"]
print(longestCommonPrefix(strs))
