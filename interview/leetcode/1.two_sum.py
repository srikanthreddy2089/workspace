#https://leetcode.com/problems/two-sum/
"""
During iteration insert the target - current element into hashmap, and in next iteration
check if element present in hashmap, if not insert again target - current element into hash map. 
"""

def two_sum(nums, target):
    hash_map = {}
    for pos in range(len(nums)):
        if nums[pos] in hash_map:
            return [hash_map[nums[pos]],pos]
        hash_map[target - nums[pos]] = pos

print(two_sum(nums = [2,7,11,15], target = 9))