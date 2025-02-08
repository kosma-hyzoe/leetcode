"""
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k]
== 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums):

        triplets = []
        nums.sort()

        # if nums[0] == 0:
        #     return [[0, 0, 0]] if nums[:3] == [0, 0, 0] else []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            right = len(nums) - 1
            left = i + 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

        return triplets
