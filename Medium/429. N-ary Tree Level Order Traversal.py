class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
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
            
                for child in node.children:
                    if child:
                        next_queue.append(child)  
            
            queue = next_queue 
            level+=1
        return level_list

#Runtime: 52 ms, faster than 63.70% of Python3 online submissions for N-ary Tree Level Order Traversal.
#Memory Usage: 15.9 MB, less than 17.30% of Python3 online submissions for N-ary Tree Level Order Traversal.
#Fu-Ti, Hsu 
#shifty049@gmail.com