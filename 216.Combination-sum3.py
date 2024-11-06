class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        possible_set = [n for n in range(1,10)]
        res = []

        def backTrack(currRes, size, target, possible_set):        
            if len(currRes) == size and sum(currRes) == target:
                res.append(currRes)
                return
            
            elif len(currRes) >= k:
                return

            for i in range(len(possible_set)):
                backTrack(currRes + [possible_set[i]], size, target, possible_set[i+1:])

        if n != 0:
            backTrack([], k, n, possible_set) 

        return res
      
