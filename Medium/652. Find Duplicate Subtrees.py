# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        self.ans = []
        self.visited = {}
        
        def helper(r):
            
            if r:
                left = helper(r.left)
                right = helper(r.right)
                record = '.'.join([str(r.val), left, right])
                if record not in self.visited:
                    self.visited[record] = 1
                else:
                    self.visited[record] += 1
                    if self.visited[record] == 2:
                        self.ans.append(r)
                        
                return record
            else:   
                return ''
                
        helper(root)
        return self.ans

#Runtime: 56 ms, faster than 98.42% of Python3 online submissions for Find Duplicate Subtrees.
#Memory Usage: 22.1 MB, less than 71.51% of Python3 online submissions for Find Duplicate Subtrees.
#Fu-Ti, Hsu 
#shifty049@gmail.com