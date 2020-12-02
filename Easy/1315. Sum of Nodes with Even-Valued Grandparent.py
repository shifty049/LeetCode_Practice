class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sumer= 0
        
        def dfs(n,path):
            if len(path)>2 and not path[-3] %2:
                self.sumer+=  path[-1]
         
            if n.left:
                dfs(n.left,path+[n.left.val])
            if n.right:
                dfs(n.right,path+[n.right.val])
            
      
            return self.sumer
        
        return dfs(root,[root.val])

#Runtime: 88 ms, faster than 97.52% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
#Memory Usage: 17.8 MB, less than 9.18% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
#Fu-Ti, Hsu 
#shifty049@gmail.com
