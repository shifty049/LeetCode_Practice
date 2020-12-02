class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
       
        def dfs(n, path):
            if not n:
                return self.count
            
            if not path or (n.val >= max(path)):
                self.count+=1     
                
            dfs(n.left, path+[n.val])
            dfs(n.right, path+[n.val])

            return self.count
        
        return dfs(root, [])

#Runtime: 348 ms, faster than 6.29% of Python3 online submissions for Count Good Nodes in Binary Tree.
#Memory Usage: 33.6 MB, less than 8.42% of Python3 online submissions for Count Good Nodes in Binary Tree.
#Fu-Ti, Hsu 
#shifty049@gmail.com