'''

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take course
ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to
    first take course 1.

Return true if you can finish all courses. Otherwise, return false.

https://leetcode.com/problems/course-schedule
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        if not prerequisites:
            return True

        prerequisites_count = [0] * numCourses
        prerequisites_list = {}

        for a, b in prerequisites:
            prerequisites_count[a] += 1
            if b not in prerequisites_list:
                prerequisites_list[b] = []
            prerequisites_list[b].append(a)

        q = []
        for c in range(numCourses):
            if prerequisites_count[c] == 0:
                q.append(c)

        courses_taken = 0
        while q:
            curr = q.pop(0)
            courses_taken += 1

            if not prerequisites_list.get(curr):
                continue
            for c in prerequisites_list[curr]:
                prerequisites_count[c] -= 1

                if prerequisites_count[c] == 0:
                    q.append(c)
        return courses_taken == numCourses
