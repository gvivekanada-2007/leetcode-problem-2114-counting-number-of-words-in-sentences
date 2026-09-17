class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
    
        ans = [1]*len(nums)
        n = len(nums)//2
        for i in range(n):
            ans[i*2] = nums[i]
            ans[2*i+1] = nums[n+i]
        return ans