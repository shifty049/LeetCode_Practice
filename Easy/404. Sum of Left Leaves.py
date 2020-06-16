# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sumer=0
        def dfs(r): 
            if not r:
                return            
            if r.left and not r.left.left and not r.left.right:
                self.sumer+=r.left.val
                
            dfs(r.left)
            dfs(r.right)
        dfs(root)    
        return self.sumer
#Runtime: 20 ms, faster than 99.56% of Python3 online submissions for Sum of Left Leaves.
#Memory Usage: 14.4 MB, less than 42.87% of Python3 online submissions for Sum of Left Leaves.
#Fu-Ti, Hsu 
#shifty049@gmail.com