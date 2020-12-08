class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        level_sum_dict = {}
        
        queue = [root]        
        
        level = 1
        max_level = 1
        while queue:
            
            next_queue = []
            
            for node in queue:
                
                if level not in level_sum_dict: 
                    level_sum_dict[level] = node.val
                else:
                    level_sum_dict[level]+= node.val
                
                if node.left:
                    next_queue.append(node.left)
                
                if node.right:
                    next_queue.append(node.right)
            
            if level > 1 and level_sum_dict[level] > level_sum_dict[max_level]:
                max_level = level
            
            level+=1
            queue = next_queue
        
        
        return max_level

#Runtime: 284 ms, faster than 86.71% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
#Memory Usage: 18.6 MB, less than 10.26% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
#Fu-Ti, Hsu 
#shifty049@gmail.com