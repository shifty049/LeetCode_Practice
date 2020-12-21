# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
    
        queue = [root]
        
        lst = []
        
        level = 0
        while queue:
            
            lst.append([])
            new_queue = []
            for node in queue:
                
                if not lst[level]: 
                    if level%2:
                        if not node.val%2:
                            lst[level].append(node.val)
                        else:
                            return False
                    else:
                        if node.val%2:
                            lst[level].append(node.val)
                        else:
                            return False
                else:
                    if level%2:
                        if not node.val%2 and node.val < lst[level][-1]:
                            lst[level].append(node.val)
                        else:
                            return False
                        
                    else:              
                        if node.val%2 and node.val > lst[level][-1]:
                                lst[level].append(node.val)
                        else:
                            return False
                    
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                
            queue = new_queue
            
            level+=1
        
        return True

#Runtime: 504 ms, faster than 67.39% of Python3 online submissions for Even Odd Tree.
#Memory Usage: 45.9 MB, less than 30.78% of Python3 online submissions for Even Odd Tree.
#Fu-Ti, Hsu 
#shifty049@gmail.com 