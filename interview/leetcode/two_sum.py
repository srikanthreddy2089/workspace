#https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    hash_map = {}
    for pos in range(len(nums)):
        if nums[pos] in hash_map:
            return hash_map[nums[pos]],pos
        check_for = target - nums[pos]
        hash_map[check_for] = pos
print(two_sum(nums = [2,7,11,15], target = 26))