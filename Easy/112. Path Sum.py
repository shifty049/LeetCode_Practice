class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        self.check = False
        
        def dfs(n, sumer):
          
            if n.left:
                dfs(n.left, sumer+n.left.val)
            if n.right:
                dfs(n.right, sumer+n.right.val)
            
            if not n.left and not n.right and sumer == sum:            
                    self.check = True
            return self.check
        
        return dfs(root, root.val)
#Runtime: 32 ms, faster than 98.45% of Python3 online submissions for Path Sum.
#Memory Usage: 16 MB, less than 9.49% of Python3 online submissions for Path Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com