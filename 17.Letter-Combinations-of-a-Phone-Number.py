class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2" : "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9":"wxyz" }
        res = []


        def backTrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return 
            
            for c in dic[digits[i]]:
                backTrack(i + 1, currStr+c)
            


        if digits:
            backTrack(0, '')

        return res

                    





                


                

        
            


    

