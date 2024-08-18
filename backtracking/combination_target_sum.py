#!/usr/bin/python3

"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.
"""

from array import array


class Solution:
    def combinationSum(self, nums, target):
        comb = []

        def backtrack(i, curr, sum):
            if sum == target:
                comb.append(list(curr).copy())
                return
            if sum > target:
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                print(j, "\t", curr)
                backtrack(j, curr, sum + nums[j])
                curr.pop()
                print(j, "\t", curr)

        backtrack(0, array('b'), 0)
        return comb


print(Solution().combinationSum([2, 3, 6, 7, 1], 7))
