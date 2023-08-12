class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0
        while(j <= len(prices)-1):
            if((prices[j] - prices[i]) >= 1):
                profit += (prices[j] - prices[i] )
            i+=1
            j +=1
        
        return profit
