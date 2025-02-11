from queue import Queue


class Solution:
    def validTree(self, n: int, edges):
        nbrs = {}

        for a, b in edges:
            if a in nbrs:
                nbrs[a].append(b)
            else:
                nbrs[a] = [b]
            if b in nbrs:
                nbrs[b].append(a)
            else:
                nbrs[b] = [a]

        for d in nbrs:
            print(d, nbrs[d])

        q = Queue([0])
        vis = set()
        while q:
            c = q.pop()

        def bfs(i):
            if i in vis:
                return
            vis.add(i)

            for nbr in nbrs[i]:
                if cur == 2:
                    print(nbr)
                if nbr == cur:
                    return 1
                bfs(nbr)

        for i in range(n):
            cur = i
            if bfs(i):
                return False
            vis = set()

        return True
