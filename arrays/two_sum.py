"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):

        val_index = {}
        for i in range(0, len(nums)):
            if target - nums[i] in val_index:
                return [val_index[target - nums[i]], i]
            val_index[nums[i]] = i
