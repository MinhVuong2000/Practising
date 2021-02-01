class Solution:
def subarraySum(self, nums: List[int], k: int) -> int:
    dic = {0:1}
    res = summ = 0
    for value in nums:
        summ+=value
        res += dic.get(summ-k,0)
        dic[summ] = dic.get(summ, 0) + 1
    return res
