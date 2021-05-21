class CustomStack:

    def __init__(self, maxSize: int):
        
        self.stack = []
        
        self.maxSize = maxSize
        
        self.length = 0

    def push(self, x: int) -> None:
        
        if self.length < self.maxSize:
            
            self.stack.append(x)
            
            self.length += 1
        

    def pop(self) -> int:
        
        if self.length:
            
            self.length -= 1
            
            return self.stack.pop()
        
        return -1
        

    def increment(self, k: int, val: int) -> None:
        
        self.stack = [v + val for v in self.stack[:k]] + self.stack[k:]
        
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

#Runtime: 116 ms, faster than 79.72% of Python3 online submissions for Design a Stack With Increment Operation.
#Memory Usage: 15.2 MB, less than 5.73% of Python3 online submissions for Design a Stack With Increment Operation.
#Fu-Ti, Hsu 
#shifty049@gmail.com