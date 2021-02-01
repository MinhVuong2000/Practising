class Solution:
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (grid[r][c]=="1"):
                count+=1
                self.dfs(grid,r,c)
    return count
                
                
def dfs(self,grid: List[List[str]],r,c):
    if (0 <= r <len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=="1"):
        grid[r][c]="0"
        self.dfs(grid,r,c+1)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r,c-1)
