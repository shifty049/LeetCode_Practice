# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        
        self.r = root
        self.dict = {0: []}
        self.cur = 0
        n = [root]
        
        while n:
            new_n = []
            
            for r in n:
                if len(self.dict[self.cur]) < 2 ** self.cur:
                    self.dict[self.cur].append(r)
                else:
                    self.cur += 1
                    self.dict[self.cur] = [r]
                
                if self.cur > 0:
                    idx = len(self.dict[self.cur]) - 1
                    if not idx % 2:
                        self.dict[self.cur - 1][idx // 2].left = r
                    else:
                        self.dict[self.cur - 1][idx // 2].right = r
                
                if r.left:
                    new_n.append(r.left)
                if r.right:
                    new_n.append(r.right)
            n = new_n
    
    def insert(self, val: int) -> int:
        r = TreeNode(val)
        
        if len(self.dict[self.cur]) < 2 ** self.cur:
            self.dict[self.cur].append(r)
        else:
            self.cur += 1
            self.dict[self.cur] = [r]
        
        idx = len(self.dict[self.cur]) - 1
        if not (len(self.dict[self.cur]) - 1) % 2:
            self.dict[self.cur - 1][idx // 2].left = r
        else:
            self.dict[self.cur - 1][idx // 2].right = r
        
        return self.dict[self.cur - 1][idx // 2].val
        
    def get_root(self) -> Optional[TreeNode]:
        return self.r
        
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

#Runtime: 68 ms, faster than 85.77% of Python3 online submissions for Complete Binary Tree Inserter.
#Memory Usage: 15.2 MB, less than 33.13% of Python3 online submissions for Complete Binary Tree Inserter.
#Fu-Ti, Hsu 
#shifty049@gmail.com