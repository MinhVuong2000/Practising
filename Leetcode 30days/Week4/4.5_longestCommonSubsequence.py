class Solution:
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    len1, len2 = len(text1), len(text2)
    dp=[[0]*(len2+1) for _ in range (len1+1)]
    for i1 in range (len1):
        for i2 in range(len2):
            if text1[i1]==text2[i2]:
                dp[i1+1][i2+1] = dp[i1][i2]+1
            else:
                dp[i1+1][i2+1] = max(dp[i1][i2+1],dp[i1+1][i2])
    return dp[-1][-1]
