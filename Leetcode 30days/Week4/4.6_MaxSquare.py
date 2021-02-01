class Solution:
def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    max_square = 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range (rows)]
    for r in range(rows):
        for c in range (cols):
            if matrix[r][c]=="1":
                if c!=0 and r!=0:
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1])+1
                else:
                    dp[r][c] = 1
                max_square = max(max_square, dp[r][c])
    return max_square**2
