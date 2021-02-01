class Solution:
def max(x,y):
    return x if x>y else y
def maxSubArray(self, nums: List[int]) -> int:
    local_max, global_max = 0, None
    for num in nums:
        global_max = local_max+num if global_max==None else max(global_max, local_max+num)
        print
        local_max = max(0, local_max+num)
    return global_max
