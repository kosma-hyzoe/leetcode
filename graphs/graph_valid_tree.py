class Solution:
    def validTree(self, n: int, edges):
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

