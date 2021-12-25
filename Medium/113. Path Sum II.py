# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.tot = []
        def helper(r, path, sumer):
            
            if r:
                sumer += r.val
                
                if not r.left and not r.right:
                    if sumer == targetSum:
                        self.tot.append(path + [r.val])
                else:
                    if r.left:
                        helper(r.left, path + [r.val], sumer)
                    
                    if r.right:
                        helper(r.right, path + [r.val], sumer)
        
        helper(root, [], 0)
         
        return self.tot

#Runtime: 36 ms, faster than 97.22% of Python3 online submissions for Path Sum II.
#Memory Usage: 19.4 MB, less than 21.07% of Python3 online submissions for Path Sum II.
#Fu-Ti, Hsu 
#shifty049@gmail.com