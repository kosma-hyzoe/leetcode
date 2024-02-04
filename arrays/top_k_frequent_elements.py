# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        freqs = sorted(list(Counter(nums).items()), key=lambda x: x[1])
        return [freqs.pop()[0] for i in range(0, k)]
