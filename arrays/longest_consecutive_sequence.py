# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = set(nums)

        longest = 1
        for n in nums:
            curr_n = n
            curr_l = 1
            if n - 1 not in nums:
                while curr_n + 1 in nums:
                    curr_l += 1
                    curr_n += 1
                if curr_l > longest:
                    longest = curr_l
        return longest
