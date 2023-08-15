"""
https://leetcode.com/problems/valid-anagram/submissions/
"""


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sc = defaultdict(int)
        tc = defaultdict(int)
        for sl, tl in zip(s, t):
            sc[sl] += 1
            tc[tl] += 1

        return sc == tc


