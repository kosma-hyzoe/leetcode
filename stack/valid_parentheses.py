# https://leetcode.com/problems/valid-parentheses

MATCH = {'(': ')', '{': '}', '[': ']'}


class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        st = [s.pop(0)]
        if st[0] in MATCH.values():
            return False

        while s:
            p = s.pop(0)
            if p in MATCH:
                st.append(p)

            if not st:
                return False
            elif p == MATCH[st[-1]]:
                st.pop()
            elif p in MATCH.values():
                return False
        return False if st else True


if __name__ == "__main__":
    import sys
    s = Solution()
    print(s.isValid(sys.argv[1]))
