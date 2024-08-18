# https://leetcode.com/problems/3sum

"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i !=j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
"""


class Solution:
    def threeSum(self, nums):
        sol = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

                l, r = i + 1, len(nums) - 1
                while l < r:
                    threeSum = v + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        sol.append([nums[l], v, nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

print(Solution().threeSum([0, 1, 1]))
