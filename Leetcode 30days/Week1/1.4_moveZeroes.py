class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        idx_0=0
        idx_not0=0
        while(idx_0<n and idx_not0<n):
            while(idx_0<n):
                if nums[idx_0]==0:
                    break
                else: idx_0=idx_0+1
            while(idx_not0<n):
                if nums[idx_not0]!=0:
                    break
                else: idx_not0=idx_not0+1
            if (idx_0 < idx_not0 and idx_not0<n):
                nums[idx_0],nums[idx_not0] = nums[idx_not0],nums[idx_0]
                idx_0+=1
            idx_not0+=1
            
        """good solution
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        """