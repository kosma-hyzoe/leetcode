# https://leetcode.com/problems/3sum

"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i !=j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
"""


class Solution:
    def threeSum(self, nums):
        def _sum():
            return nums[li] + nums[ri]

        def _3rd(li, ri):
            return 0 - (nums[li] + nums[ri])

        thirds = []
        lenn = len(nums)
        nums = sorted(nums)

        li = 0
        ri = lenn - 1

        while nums[li] < 0 and li != ri:
            third = _3rd(li, ri)
            if third in nums[li + 1:ri]:
                thirds.append([nums[li], third, nums[ri]])

            if third > nums[ri]:
                li += 1
            else:
                ri += 1

        return thirds
