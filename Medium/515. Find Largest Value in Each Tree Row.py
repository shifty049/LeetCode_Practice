class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if not root:
            return root
        
        queue = [root]
        level = 0
        level_dict = {}
        
        while queue:
            next_queue = []  
            for node in queue:
                
                if level not in level_dict:
                    level_dict[level] = node.val           
                else:
                    level_dict[level] = max( level_dict[level], node.val)  
                
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            queue = next_queue 
            level+=1
        
        return list(level_dict.values())

#Runtime: 36 ms, faster than 98.20% of Python3 online submissions for Find Largest Value in Each Tree Row.
#Memory Usage: 16.3 MB, less than 41.45% of Python3 online submissions for Find Largest Value in Each Tree Row.
#Fu-Ti, Hsu 
#shifty049@gmail.com