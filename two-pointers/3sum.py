# https://leetcode.com/problems/3sum

"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i !=j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
"""


class Solution:
    def threeSum(self, nums):
        triplets = []

        li = 0
        visited = []
        nums = sorted(nums)
        ri = len(nums) - 1

        print(nums)
        while True:
            if nums[li] not in visited:
                visited.append(nums[li])

                tri_visited = []
                for tri in range(ri, li + 1, -1):
                    if nums[tri] in tri_visited:
                        continue
                    tri_visited.append(nums[tri])

                    third = 0 - (nums[li] + nums[tri])
                    if third in nums[li + 1:tri]:
                        triplets.append([nums[li], third, nums[tri]])

            if li == ri - 2 or nums[li + 1] > 0:
                return triplets
            li += 1


print(Solution().threeSum([-1,0,1,2,-1,-4]))
