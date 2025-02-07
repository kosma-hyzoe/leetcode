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

        prev = 'f'
        for i in range(len(nums) - 2):

            if nums[i] == prev:
                prev = nums[i]
                continue
            else:
                prev = nums[i]

            right = len(nums) - 1
            prev_left = 'f'
            left = i + 1
            while left < len(nums) - 1 and right != left:
                if prev_left == nums[left]:
                    right = len(nums) - 1
                    prev_left = nums[left]
                    left += 1
                    continue
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    if right == left:
                        break
                    prev_left = nums[left]
                    left += 1

                elif sum < 0:
                    prev_left = nums[left]
                    left += 1
                elif sum > 0:
                    right -= 1

        return triplets
