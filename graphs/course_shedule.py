from queue import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        if len(prerequisites) == 0:
            return True
        preq_dict = {}

        for cou, pre in prerequisites:
            if cou not in preq_dict:
                preq_dict[cou] = set([pre])
            else:
                preq_dict[cou].add(pre)

        taken = set()
        to_take = deque()
        for i in range(numCourses):
            if i in preq_dict:
                to_take.append(i)
            else:
                taken.add(i)

        vis = set()

        def bfs(course):
            if course in vis:
                return
            vis.add(course)

            preqs = preq_dict[course]
            preqs = deque([c for c in preqs if c not in taken])
            while preqs:
                if not bfs(preqs.popleft()):
                    return False

            taken.add(course)
            return True

        for c in to_take:
            if not bfs(c):
                return False

        return True


p = [[0, 1], [0, 2], [1, 2]]
n = 3
print(Solution().canFinish(n, p))
