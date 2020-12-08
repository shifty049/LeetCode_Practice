class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.dict = {}       
        queue = [root]	
		level = 0
		
        # result= {node_value:[parent,level]}
		result = {root.val:[None, level]}
        	
        while queue:
            level+=1
            next_queue = []
            for node in queue:
                if node.left:
                    result[node.left.val] = [node.val,level]
                    next_queue.append(node.left)
                if node.right:
                    result[node.right.val] = [node.val,level]
                    next_queue.append(node.right)
            queue = next_queue
        
        return result[x][0]!= result[y][0] and result[x][1] == result[y][1]

#Runtime: 24 ms, faster than 97.01% of Python3 online submissions for Cousins in Binary Tree.
#Memory Usage: 14.4 MB, less than 7.73% of Python3 online submissions for Cousins in Binary Tree.
#Fu-Ti, Hsu 
#shifty049@gmail.com