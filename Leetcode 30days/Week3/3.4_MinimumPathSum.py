class Solution:
def minPathSum(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    res = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r==0:
                if c==0:
                    res[r][c] = grid[r][c]
                else:
                    res[r][c] = res[r][c-1] + grid[r][c]
            else:
                if c==0:
                    res[r][c] = res[r-1][c] + grid[r][c]
                else:
                    res[r][c] = min(res[r][c-1], res[r-1][c]) + grid[r][c]
    return res[-1][-1]
