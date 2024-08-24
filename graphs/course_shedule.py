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

            q = deque(preq_dict[course])
            while q:
                curr = q.popleft()
                preqs = preq_dict[curr]
                preqs = [c for c in preqs if c not in taken]

                if len(to_take) == 0:
                    taken.add(curr)
                    if len(taken) >= numCourses:
                        return True
                else:
                    q.extend([cc for cc in to_take if cc not in vis])
            if

        for c in to_take():
            bfs(c)


p = [[0, 1], [0, 2], [1, 2]]
n = 3
print(Solution().canFinish(n, p))
