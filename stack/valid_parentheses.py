# https://leetcode.com/problems/valid-parentheses

MATCH = {'}': '{', ']': '[', ')': '('}


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in MATCH:
                if st and st[-1] == MATCH[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c


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
