class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return root
        
        queue = [root]
        
        result_lst = []
        
        level = 0
        
        while  queue:
            next_queue = []
            result_lst.append(queue[-1].val)
            
            for node in queue:            
    
                if node.left:
                    next_queue.append(node.left)
                
                if node.right:
                    
                    next_queue.append(node.right)
                
            queue = next_queue
            level+=1
        
        return result_lst

#Runtime: 28 ms, faster than 85.99% of Python3 online submissions for Binary Tree Right Side View.
#Memory Usage: 14.3 MB, less than 13.80% of Python3 online submissions for Binary Tree Right Side View.
#Fu-Ti, Hsu 
#shifty049@gmail.com
