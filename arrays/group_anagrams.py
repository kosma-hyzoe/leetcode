# https://leetcode.com/problems/group-anagrams

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            cc = 26 * [0]
            for c in s:
                cc[ord(c) - ord('a')] += 1
            groups[tuple(cc)].append(s)

        return groups.values()
