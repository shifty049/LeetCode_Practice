class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        l = []
        
        def dfs(root,path):
            if root:
               
                if not root.left and not root.right:
                    l.append(path+[str(root.val)])
                    return l

                dfs(root.left,path+[str(root.val)])
                dfs(root.right,path+[str(root.val)])
            return l
        
        return ['->'.join(item) for item in dfs(root,[])]

#Runtime: 36 ms, faster than 28.46% of Python3 online submissions for Binary Tree Paths.
#Memory Usage: 14.3 MB, less than 15.74% of Python3 online submissions for Binary Tree Paths.
#Fu-Ti, Hsu 
#shifty049@gmail.com