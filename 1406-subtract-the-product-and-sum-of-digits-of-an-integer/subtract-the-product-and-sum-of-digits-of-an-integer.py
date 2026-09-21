class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        k = 0
        b = 1
        while n!=0:
            last_digit = n%10
            k = k+last_digit
            b = b*last_digit
            n = n//10
        return b-k