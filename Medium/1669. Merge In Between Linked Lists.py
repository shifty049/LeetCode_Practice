class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        ix = 0
       
        while True:
    
            if ix == 0:

                head = list1
            if ix ==a-1:
                lst1_head = list1

            if ix == b +1:

                lst1_tail = list1
                break

            list1 = list1.next
                
            ix+=1
        
        lst2_head = list2
        
        while list2:
               
            if not list2.next:
                
                lst2_tail = list2
            list2= list2.next

        lst1_head.next = lst2_head
        lst2_tail.next = lst1_tail
        
        return head

#Runtime: 456 ms, faster than 51.12% of Python3 online submissions for Merge In Between Linked Lists.
#Memory Usage: 20.1 MB, less than 36.68% of Python3 online submissions for Merge In Between Linked Lists.
#Fu-Ti, Hsu 
#shifty049@gmail.com