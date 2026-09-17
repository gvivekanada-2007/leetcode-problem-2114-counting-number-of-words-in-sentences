class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        ans = []
        for i in range(len(nums)):
            L = 0
    
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    L = L+1
            ans.append(L)
        return ans
    
