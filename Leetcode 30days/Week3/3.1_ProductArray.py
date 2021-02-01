##space complex O(n)
class Solution:
def productExceptSelf(self, nums: List[int]) -> List[int]:
    left, right = [1]*len(nums), [1]*len(nums)
    
    # build left
    for i in range(1, len(nums)):
        left[i] = left[i-1]*nums[i-1]

    # build right
    for i in reversed(range(0, len(nums)-1)):
        right[i] = right[i+1]*nums[i+1]
        
    # build final list
    for i in range(len(nums)):
        nums[i] = left[i]*right[i]
        
    return nums
    
    
##time: O(1)
def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            res[~i] *= rprod
            rprod *= nums[~i]
            print(res[i],lprod,res[~i],rprod)
        return res
