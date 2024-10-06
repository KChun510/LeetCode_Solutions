class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: return
        curr = root

        while(curr != None): 
            if curr.left != None:
                deepestRight = curr.left
                while(deepestRight.right != None):
                    deepestRight = deepestRight.right
                    
                deepestRight.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right

"""
Gernal idea: Take a left. Then find first leaf with a right side. Travserse fully down the this leaf until the right mode node, starting from the left side.


When at the right most. Append the root nodes right side, to the left right most bottom node. Then re-assign roots right side to our appended tree, on the left.

Last re-assign left to None
"""
 
