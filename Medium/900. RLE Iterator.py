# Solution 1
from collections import deque
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.raw = dict()
        self.idx_dict = {}
        for ix, i in enumerate(encoding):
            
            if ix % 2:
                if str(i) not in self.raw:
                    self.idx_dict[str(i)] = 0
                    self.raw[str(i)] = encoding[ix - 1] 
                else:
                    
                    self.raw['{}_{}'.format(str(i), self.idx_dict[str(i)])] = encoding[ix - 1]
                    self.idx_dict[str(i)] += 1
                            
        self.check = deque(self.raw.keys())
        
        self.exam = self.check.popleft()
    def next(self, n: int) -> int:
       
        while self.raw and n:  
            
            if self.raw[self.exam] > n:
               
                self.raw[self.exam] -= n
                
                return int(self.exam.split('_')[0])           
            else:
                n -= self.raw[self.exam]
                del self.raw[self.exam]         
                
                prev_exam = int(self.exam.split('_')[0])
                
                if self.check:
                        self.exam = self.check.popleft()
                        
                if not n:
                    return prev_exam
                    
        return -1
            
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

            
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

#Runtime: 32 ms, faster than 93.47% of Python3 online submissions for RLE Iterator.
#Memory Usage: 14.8 MB, less than 88.39% of Python3 online submissions for RLE Iterator.
#Fu-Ti, Hsu 
#shifty049@gmail.com


# Solution 2
from collections import deque
class RLEIterator:

    def __init__(self, encoding: List[int]):
        
        self.A = encoding
    
    def next(self, n: int) -> int:
        
        self.index = 0
        
        while self.index < len(self.A) and n:
            
            if self.A[self.index] > n:
                
                self.A[self.index] -= n
                
                n = 0
                
                ans = self.A[self.index + 1]
            
            else:
                n -= self.A[self.index]
                
                if not n:
                    ans = self.A[self.index + 1]
                
                self.index += 2
        
        self.A = self.A[self.index:]
        
        if not n:
            return ans
        
        if not self.A:
            return -1
            
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

#Runtime: 40 ms, faster than 55.09% of Python3 online submissions for RLE Iterator.
#Memory Usage: 14.7 MB, less than 96.10% of Python3 online submissions for RLE Iterator.
#Fu-Ti, Hsu 
#shifty049@gmail.com
