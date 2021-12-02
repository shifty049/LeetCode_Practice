"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
                
        if not root:
            return root
        
        queue = [root] 
                 
        while queue:
            
            new_queue = []
            for ix, nde in enumerate(queue):
                    
                if nde.left:
                
                    new_queue.extend([nde.left, nde.right])  
                             
                else:
                    return root
    
            for jx, j in enumerate(new_queue[:-1]):
                
                    j.next = new_queue[jx + 1]
                
            queue = new_queue

#Runtime: 64 ms, faster than 65.95% of Python3 online submissions for Populating Next Right Pointers in Each Node.
#Memory Usage: 15.5 MB, less than 99.34% of Python3 online submissions for Populating Next Right Pointers in Each Node.
#Fu-Ti, Hsu 
#shifty049@gmail.com