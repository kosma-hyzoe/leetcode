# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s):
        s = "".join(c.lower() for c in s if c.isalnum())
        lens = len(s)
        pr = 0
        pl = lens - 1

        if lens < 2:
            return True

        while pr < pl:
            print(s[pr], s[pl])
            if s[pr] != s[pl]:
                return False
            pr += 1
            pl -= 1

        return True
