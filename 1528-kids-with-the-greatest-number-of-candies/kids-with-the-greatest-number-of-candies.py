class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        #num = [2,0,5,1,3]
        #original = num
        k = 0
        #extra = 3
        result = []

        for i in range(len(candies)):
            k = max(k,candies[i])
        print(k)
        for j in range(len(candies)):
            candies[j] = candies[j]+extraCandies
            if candies[j]>=k:
                result.append(True)
            else:
                result.append(False)
        return result