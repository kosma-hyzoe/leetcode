#!/usr/bin/python3

from threesum_take2 import Solution


sol = Solution()


def debug(x, y):
    f = Solution().threeSum(x)
    if f != y:
        print(">", x, y)
        for li in f:
            print(li)


x = [-1, 0, 1, 2, -1, -4]
y = [[-1, -1, 2], [-1, 0, 1]]
debug(x, y)
x = [1, -1, -1, 0]
y = [[-1, 0, 1]]
debug(x, y)
x = [-2, 0, 1, 1, 2]
y = [[-2, 0, 2], [-2, 1, 1]]
debug(x, y)
x = [-1, 0, 1, 0]
y = [[-1, 0, 1]]
debug(x, y)
