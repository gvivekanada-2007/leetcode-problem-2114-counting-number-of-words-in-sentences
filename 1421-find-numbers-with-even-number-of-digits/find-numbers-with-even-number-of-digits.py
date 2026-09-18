class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        #nums = [12,345,23,6,7896]
        L = 0
        for i in range(len(nums)):
            k = nums[i]
            y = 0
            while k!=0:
                last_digit = nums[i]%10
                y = y+1
                k = k//10
            if y%2==0:
                L = L+1 
        return L
