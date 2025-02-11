

class Solution:
    def validTree(self, n: int, edges):
        nbrs = {}
        cur = None
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
        # for d in nbrs:
        #     print(d, nbrs[d])

        def dfs(i, p):
            if i in vis or len(nbrs[i]) == 1:
                return
            vis.add(i)

            for nbr in nbrs[i][::-1]:
                if nbr in vis:
                    return 1
                dfs(nbr, i)

        for i in nbrs:
            cur = i
            # print(cur)
            if dfs(cur, None):
                return False
            vis = set()

        return True
