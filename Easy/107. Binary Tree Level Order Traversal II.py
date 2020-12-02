class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        self.dict = {}
        def accumulate_level(n, level):
            
            if not n:
                return self.dict
            
            
            if level not in self.dict:
                self.dict[level] = [n.val]
            else:
                self.dict[level].append(n.val)
            accumulate_level(n.left, level+1)
            accumulate_level(n.right, level+1)
            return self.dict
            
        return list(accumulate_level(root, 0).values())[::-1]

#Runtime: 32 ms, faster than 80.61% of Python3 online submissions for Binary Tree Level Order Traversal II.
#Memory Usage: 15.2 MB, less than 6.75% of Python3 online submissions for Binary Tree Level Order Traversal II.
#Fu-Ti, Hsu 
#shifty049@gmail.com