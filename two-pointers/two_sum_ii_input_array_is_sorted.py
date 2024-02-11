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

        def _sum():
            return numbers[li] + numbers[ri]

        sum = _sum()
        while sum > target:
            ri -= 1
            sum = numbers[li] + numbers[ri]
            if sum == target:
                return [li + 1, ri + 1]
        while sum > target:
            li += 1
            sum = numbers[li] + numbers[ri]
            if sum == target:
                return [li + 1, ri + 1]

        while True:
            sum = numbers[li] + numbers[ri]
            if sum < target:
                li += 1
            elif sum > target:
                ri -= 1
            else:
                return [li + 1, ri + 1]

        return -1


assert Solution().twoSum([5, 25, 75], 100) == [2, 3]
