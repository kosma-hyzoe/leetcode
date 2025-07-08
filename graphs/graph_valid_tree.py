class Solution:
    def validTree(self, n: int, edges):
<<<<<<< HEAD
        nbrs = {}
        vis = set()

        for a, b in edges:
            if a in nbrs:
                nbrs[a].append(b)
            else:
                nbrs[a] = [b]
            if b in nbrs:
                nbrs[b].append(a)
            else:
                nbrs[b] = [a]

        # print(nbrs)
        for d in nbrs:
            print(d, nbrs[d])

        def dfs(cur, prev):
            print(cur, prev)
            if cur in vis:
                return
            elif len(nbrs[cur]) == 1:
                vis.add(cur)
                return
            vis.add(cur)

            for nbr in nbrs[cur][::-1]:
                if nbr == prev:
                    continue
                elif nbr in vis:
                    return 1
                dfs(nbr, cur)

        for i in nbrs:
            if dfs(i, None):
                return False
        return len(vis) == n
=======
        if len(edges) > (n - 1):
            return False

        nbrs = [[] for _ in range(n)]
        for u, v in edges:
            nbrs[u].append(v)
            nbrs[v].append(u)

        vis = set()

        def dfs(cur, prev):
            if cur in vis:
                return False
            vis.add(cur)

            for nbr in nbrs[cur]:
                if nbr == prev:
                    continue
                if not dfs(nbr, cur):
                    return False
            return True

        return dfs(0, -1) and len(vis) == n
>>>>>>> 0dd4e73b320806c370e4d17f6dfdb077c37ea6b3

