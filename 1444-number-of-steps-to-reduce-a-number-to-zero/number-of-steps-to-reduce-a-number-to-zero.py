class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        b = 0
        k = 0
        while num!=0:
            if num%2==0:
                k = k+1
                num = num//2
            else:
                num=num-1
                b = b+1
        return b+k