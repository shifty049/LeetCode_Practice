class StockSpanner:

    def __init__(self):
        
        self.l = []
    def next(self, price: int) -> int:  
        
        if not self.l:
            
            self.l.append([price, 1])
        
        else:
            if price < self.l[-1][0]:
                self.l.append([price, 1])        
            else:
                curr_n = 1 
                while self.l:
                    
                    if price >= self.l[-1][0]:
                        prv_val, prev_n = self.l.pop()
                        
                        curr_n += prev_n
                    else:
                        break
                
                self.l.append([price, curr_n])
            
        return self.l[-1][1]
            
       
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#Runtime: 440 ms, faster than 53.55% of Python3 online submissions for Online Stock Span.
#Memory Usage: 19 MB, less than 41.83% of Python3 online submissions for Online Stock Span.
#Fu-Ti, Hsu 
#shifty049@gmail.com