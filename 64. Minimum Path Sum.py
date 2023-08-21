class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        @cache
        
        def recur(m , n):
            if n < 0 or m < 0:
                return maxsize
            elif n == 0 and m == 0:
                return grid[0][0]
            
            return grid[m][n] + min(recur(m- 1, n), recur(m, n-1))

        return recur(m,n )
