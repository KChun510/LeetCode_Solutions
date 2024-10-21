class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0
        
        for elem in prices[1:]:
            if bp > elem:
                bp = elem
            profit = max(profit, elem - bp)

        return profit 
            
