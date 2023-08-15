"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution:
    def longestConsecutive(self, nums):
        has_prev = {n: False for n in nums}
        for n in nums:
            if n - 1 in has_prev:
                has_prev[n] = True

        return len([v for v in has_prev.values() if v])


Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
