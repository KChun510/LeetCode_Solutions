# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        max_path = 0 
        curr_path = 1
        right_nodes = []

        if curr == None:
            return 0

        while curr:
            if curr_path > max_path:
                max_path = curr_path
            if curr.right:
                print(curr.right.val)
            if curr.right:
                right_nodes.append([curr.right, curr_path + 1])
            if curr.left:
                curr = curr.left
                curr_path += 1
            elif len(right_nodes) > 0:
                curr = right_nodes[0][0]
                curr_path = right_nodes[0][1]
                right_nodes = right_nodes[1:]
            elif curr.right == None and curr.left == None:
                break
        return max_path
            
        
