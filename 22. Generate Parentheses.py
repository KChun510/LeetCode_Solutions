class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 
        stack = ""

        def recur(openN, closedN, stack, res):
            if openN == closedN == n: #This is our base case, if reached the end add to final res
                print(stack)
                res += [stack]
                return #Once we reach our return, we will pop back up to OG branch step A.

            if openN < n:  #Left branch tree instialization
                stack += "("
                recur(openN + 1, closedN, stack, res)  
                stack = stack[:-1] #We only pop once our recursive calls reach a return step B.
            
            if closedN < openN: #Right branch tree initialization
                stack += ")"
                recur(openN, closedN +1, stack, res)
                stack = stack[:-1] #We only pop once our recursive calls reach a return step B.
            
        recur(0, 0, stack, res)
        return res


        #Time complexity. o(2^2n) At each level of the recursion tree we'll have two choices. Which is exopential. We first start with 2 option, then for each level we have an additional 2n options.
            

        #Space complexity. O(2*n) can be simplefied to O(n) due to its linear nature. The recursion tree will only be as large as 2*n.
