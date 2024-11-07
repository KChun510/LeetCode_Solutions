class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = s[::-1]
        if s == "":
            return True
        s_stack = [char for char in s]
        first_val = s_stack[-1]
        for char in t:
            if char == first_val:
                s_stack.pop()
                if s_stack != []:
                    first_val = s_stack[-1]
                else:
                    return True
                    
        return False
            
"""        
Beats 100% in speed.
Intuition
We only need to iterate through t once, from left to right. If we see our first letter in "s" from "t", then pop it from our stack. Continue this pattern until we reach the end of "t".

If the stack isn't empty, then can safley say it's false.

Complexity
Time complexity:
O(n): For the building of our stack S
O(n): Iterating over T

Final: O(n+n) == O(n)

Space complexity:
O(n): Holding an auxillary stack thats of length S.
"""
