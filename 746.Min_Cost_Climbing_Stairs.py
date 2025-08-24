class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost_size = len(cost) - 2


        def dp(cost, index, memo = {}):
            if(index in memo): return memo[index]
            if index >= cost_size: return 0

            memo[index] = min(cost[index + 1] + dp(cost, index + 1), cost[index + 2] + dp(cost, index + 2) )
            return memo[index]
            

        return dp(cost, -1)
  
        
