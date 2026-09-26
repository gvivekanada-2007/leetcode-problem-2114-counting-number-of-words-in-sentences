class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                cost = prices[j]
                if cost<=prices[i]:
                    temp=prices[i]-cost
                    answer.append(temp)
                    break
            else:
                answer.append(prices[i])
        return answer