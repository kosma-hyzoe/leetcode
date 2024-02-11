# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s):
        pb = 0
        pe = -1

        s = "".join(c for c in s if c.isalnum())
        while pb < len(s):
            if s[pb].lower() != s[pe].lower():
                return False
            pb += 1
            pe -= 1

        return True


assert Solution().isPalindrome("A man, a plan, a canal: Panama")
