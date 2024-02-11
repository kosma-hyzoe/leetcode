# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

"""
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.
"""


class Solution:
    def twoSum(self, numbers, target):
        lenn = len(numbers)
        li = 0
        ri = lenn - 1

        while numbers[ri] > target + numbers[li]:
            ri -= 1

        while True:
            while li < lenn:
                if numbers[li] + numbers[ri] == target:
                    return [li + 1, ri + 1] if li < ri else [ri + 1, li + 1]
                li += 1
            ri -= 1

        return 1
