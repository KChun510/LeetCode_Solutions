class Solution(object):
    def divisorGame(self, n):
        def dp(n, winner = True):
            if(n == 0): return winner

            if (n - 1) % 1 == 0: 
                return dp(n - 1, not winner)
            if (n - 2) % 2 == 0: 
                return dp(n-2, not winner)

            return winner

        return dp(n)


    
