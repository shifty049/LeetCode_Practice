class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        while head:
            n = head
            head = head.next
            n.next = prev
            prev = n
        
        return prev

#Runtime: 24 ms, faster than 99.21% of Python3 online submissions for Reverse Linked List.
#Memory Usage: 15.6 MB, less than 39.30% of Python3 online submissions for Reverse Linked List.
#Fu-Ti, Hsu 
#shifty049@gmail.com
