class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        ATL, PAC = 0, 1

        pac = set()
        atl = set()

        def dfs(r, c, ocean):
            if (r, c) in pac if ocean == PAC else atl:
                return

            def in_bounds(r, c):
                return ROWS > r >= 0 and COLS > c >= 0

            adjs = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            adjs = (a for a in adjs if in_bounds(*a))
            if ocean == PAC:
                for ar, ac in adjs:
                    if heights[r][c] <= heights[ar][ac]:
                        pac.add((ar, ac))
                        if (ar, ac) not in atl:
                            dfs(ar, ac, ocean)
            else:
                for ar, ac in adjs:
                    if heights[r][c] <= heights[ar][ac]:
                        atl.add((ar, ac))
                        if (ar, ac) not in atl:
                            dfs(ar, ac, ocean)

        # north
        for c in range(COLS):
            dfs(0, c, PAC)
        # south
        for c in range(COLS):
            dfs(ROWS - 1, c, ATL)
        # west
        for r in range(ROWS):
            dfs(r, 0, PAC)
        # east
        for r in range(ROWS):
            dfs(r, COLS - 1, ATL)

        return [[r, c] for r, c in pac.intersection(atl)]
