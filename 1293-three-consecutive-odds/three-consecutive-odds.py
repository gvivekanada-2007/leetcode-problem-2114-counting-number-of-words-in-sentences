class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        total = 0
        for i in range(len(arr)):
            x =arr[i:i+3]
    
            for j in range(len(x)-2):
                    if x[j]%2!=0 and x[j+1]%2!=0 and x[j+2]%2!=0:
                        total = 1

        if total==1:
            return True
        else:
            return False

    
