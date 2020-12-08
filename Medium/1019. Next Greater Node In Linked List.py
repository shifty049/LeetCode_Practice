class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
   
        stack = []
        res = []
        ix = 0
        while head:
            stack.append((head.val,ix))
            res.append(0)
            head =  head.next
            
            if head:
                while stack:
                    if head.val > stack[-1][0]:
                        res[stack[-1][1]] = head.val
                        stack.pop()
                    else:
                        break

            ix+=1
         
        return res

#Runtime: 312 ms, faster than 88.47% of Python3 online submissions for Next Greater Node In Linked List.
#Memory Usage: 18.6 MB, less than 23.39% of Python3 online submissions for Next Greater Node In Linked List.
#Fu-Ti, Hsu 
#shifty049@gmail.com