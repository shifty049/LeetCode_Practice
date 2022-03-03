# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if not k:
            return [target.val]
        
        dic = {}
        def helper(n):
            if n.left:
                if n.val not in dic:
                    dic[n.val] = {}
                dic[n.val]['left'] = n.left.val
                if n.left.val not in dic:
                    dic[n.left.val] = {}
                dic[n.left.val]['upper'] = n.val

                helper(n.left)

            if n.right:
                if n.val not in dic:
                    dic[n.val] = {}
                dic[n.val]['right'] = n.right.val
                if n.right.val not in dic:
                    dic[n.right.val] = {}
                dic[n.right.val]['upper'] = n.val

                helper(n.right)
        
        helper(root)

        stack = [target.val]
        visited = {}
        curr_distance = 0
        
        while stack and curr_distance < k:
        
            new_stack = []
            for i in stack:
                visited[i] = True
                # print(i)
                # print(dic[i])
                if dic.get(i):
                    for next_l, val in dic[i].items():

                        if val is not None and val not in visited:
                            visited[val] = True

                            new_stack.append(val)
            curr_distance += 1
            stack = new_stack

            if curr_distance == k:
                return stack
        return []

#Runtime: 28 ms, faster than 98.41% of Python3 online submissions for All Nodes Distance K in Binary Tree.
#Memory Usage: 14.7 MB, less than 30.02% of Python3 online submissions for All Nodes Distance K in Binary Tree.
#Fu-Ti, Hsu 
#shifty049@gmail.com