#!/usr/bin/python3

class Solution:
    def permute(self, nums):
        perms = []

        def backtrack(i, curr):
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return

            for j in range(i, len(nums)):
                if nums[j] in curr:
                    continue
                curr.append(nums[j])
                backtrack(0, curr)
                curr.pop()

        backtrack(0, [])

        return perms
