class Solution:
def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1
    l = 0
    r = len(nums)-1
    while (l < r):
        index = int((l+r)/2)
        if (nums[index]==target):
            return index
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        elif nums[index]<target:
            if (nums[l]<nums[index] or nums[r]>target):
                l = index+1
            else:
                r = index-1
        else:
            if (nums[r]>nums[index] or nums[l]<target):
                r = index-1
            else:
                l = index+1
    return l if nums[l]==target else -1
            
