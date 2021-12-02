# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
         
        if depth == 1:
            M = TreeNode(val)
            M.left = root
            return M
        
        queue = [root]
        
        level = 1
        
        while queue:
            level += 1
            new_queue = []
            
            last = True
            for node in queue:
                
                if level == depth:         
                    
                    
                    if node.left:
                        old_left = node.left
                        node.left = TreeNode(val)
                        node.left.left = old_left
                        last = False
                    else:
                        node.left = TreeNode(val)
                    
                    if node.right:               
                        old_right = node.right
                        node.right = TreeNode(val)
                        node.right.right = old_right    
                        last = False
                    else:
                        node.right = TreeNode(val)
                         
                else: 
                    if node.left:
                        new_queue.append(node.left)
                    
                    if node.right: 
                        new_queue.append(node.right)
             
            if level == depth: 
                if last:
                    for q in queue:
                        q.left = q.right = TreeNode(val)
                
                return root
            
            queue = new_queue

#Runtime: 48 ms, faster than 97.18% of Python3 online submissions for Add One Row to Tree.
#Memory Usage: 16.4 MB, less than 60.19% of Python3 online submissions for Add One Row to Tree.
#Fu-Ti, Hsu 
#shifty049@gmail.com