class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        #account = [[1,5],[7,3],[3,5,5]]
        count = 0
        for i in range(len(accounts)):
            m = 0
            for j in range(len(accounts[i])):
                m = (accounts[i][j])+m
                count = max(count,m)
        return count