class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(x):
            k=1
            for i in x:
                k=k*i
            if k>0:
                return 1
            elif k<0:
                return -1
            else:
                return 0
        return signFunc(nums)