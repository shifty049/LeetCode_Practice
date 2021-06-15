class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.borw = [homepage]
        
        self.check_current = False

    def visit(self, url: str) -> None:
        
        if not self.check_current:
            self.borw.append(url)
        else:
            self.borw = self.borw[:self.idx + 1]
            
            self.borw.append(url)
            
            self.idx += 1
    
    def back(self, steps: int) -> str:
        
        if not self.check_current:
            
            self.idx = len(self.borw) - 1
            
            self.check_current = True
        
        self.idx  = max(0, self.idx - steps)
        
        return self.borw[self.idx]
    
    def forward(self, steps: int) -> str:
        
        if not self.check_current:
            self.idx = len(self.borw) - 1
            self.check_current = True
        
        
        self.idx  = min(len(self.borw) - 1, self.idx + steps)
        
        return  self.borw[self.idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

#Runtime: 216 ms, faster than 85.39% of Python3 online submissions for Design Browser History.
#Memory Usage: 16.7 MB, less than 36.87% of Python3 online submissions for Design Browser History.
#Fu-Ti, Hsu 
#shifty049@gmail.com