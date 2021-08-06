class FrontMiddleBackQueue:

    def __init__(self):
        
        self.q = []

    def pushFront(self, val: int) -> None:
        
        self.q.insert(0, val)
        

    def pushMiddle(self, val: int) -> None:
       
        d,r = divmod(len(self.q), 2)
      
        self.q.insert(len(self.q) // 2, val)
    
    def pushBack(self, val: int) -> None:
        
        self.q.append(val)
        
    def popFront(self) -> int:
        
        if self.q:
            
            return self.q.pop(0)
        
        return -1       

    def popMiddle(self) -> int:
        
        if self.q:  
            d,r = divmod(len(self.q), 2) 
            return self.q.pop(d - int(r == 0))
           
        return -1
 
    def popBack(self) -> int:
        
        if self.q:
            
            return self.q.pop()
        
        return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

#Runtime: 64 ms, faster than 96.44% of Python3 online submissions for Design Front Middle Back Queue.
#Memory Usage: 14.7 MB, less than 90.50% of Python3 online submissions for Design Front Middle Back Queue.
#Fu-Ti, Hsu 
#shifty049@gmail.com