lass Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def recur(m , n, memo = {}):
            key = f"{m}, {n}"
            if key in memo:
                return memo[key]
            elif m == 1 and n == 1:
                return 1
            elif m == 0 or n == 0:
                return 0
            
            memo[key] = recur(m-1, n, memo) + recur(m, n - 1, memo)
            return memo[key]
        
        return recur(m, n)
