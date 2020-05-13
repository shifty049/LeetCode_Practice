# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        self.check=False
        def dfs(r,v):
            
            if not r :
                return
            if not r.left and not r.right:
                v+=r.val
                if v==sum:
                    self.check=True
                return
            v+=r.val
            dfs(r.right,v)
            dfs(r.left,v)
        dfs(root,0)
        
        return self.check
#Runtime: 40 ms, faster than 82.56% of Python3 online submissions for Path Sum.
#Memory Usage: 15.6 MB, less than 5.45% of Python3 online submissions for Path Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com