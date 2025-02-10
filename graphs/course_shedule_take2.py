class Solution:
    def canFinish(self, numCourses: int, prerequisites):

        taken = set()
        preq_map = {}

        for a, b in prerequisites:
            if a not in preq_map:
                preq_map[a] = [b]
            else:
                preq_map[a].append(b)
        if not preq_map:
            return True

        for c in range(numCourses):
            if c not in preq_map:
                taken.add(c)
        # for preqs in preq_map.values():
        #     for r in preqs:
        #         if r not in preq_map:
        #             taken.add(r)

        vis = set()

        def recurse(cou):
            if cou in vis:
                return False
            vis.add(cou)
            for preq in preq_map[cou]:
                if preq not in taken:
                    if not recurse(preq):
                        return False
            taken.add(cou)
            return True

        for cou in preq_map:
            recurse(cou)

        return len(taken) == numCourses
