# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:        
        self.maxer=0
        self.n=1
        def dfs(r,n):
            if not r:
                return   
            n+=1
            if n >self.n:
                self.maxer=r.val
                self.n=n
            elif n==self.n:
                self.maxer+=r.val
            else:
                pass
            dfs(r.right,n)
            dfs(r.left,n)
        dfs(root,0)    
        return self.maxer

#Runtime: 100 ms, faster than 70.49% of Python3 online submissions for Deepest Leaves Sum.
#Memory Usage: 17.2 MB, less than 79.41% of Python3 online submissions for Deepest Leaves Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com
                