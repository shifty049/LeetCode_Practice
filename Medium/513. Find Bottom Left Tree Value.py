class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        if not root:
            return root
        
        queue = [root]
        level = 0
        level_list = []
        
        while queue:
            level_list.append([])
            next_queue = []  
            for node in queue:
                level_list[level].append(node.val)
            
                
                if node.left:
                        next_queue.append(node.left)
                if node.right:
                        next_queue.append(node.right)
            
            queue = next_queue 
            level+=1
        return level_list[-1][0]

#Runtime: 40 ms, faster than 83.94% of Python3 online submissions for Find Bottom Left Tree Value.
#Memory Usage: 16.3 MB, less than 42.32% of Python3 online submissions for Find Bottom Left Tree Value.
#Fu-Ti, Hsu 
#shifty049@gmail.com