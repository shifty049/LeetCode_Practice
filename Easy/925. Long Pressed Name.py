class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        ln=[]
        for i in name:
            if len(ln)==0:
                ln.append([i])
            else:
                if i==ln[-1][0]:
                    ln[-1].append(i)
                else:
                    ln.append([i])
        
        lt=[]
        for i in typed:
            
            if len(lt)==0:
                lt.append([i])
            else:
                if i==lt[-1][0]:
                    lt[-1].append(i)
                else:
                    if lt[-1][0]!=ln[0][0] or len(ln[0])>len(lt[-1]):
                        return False
                    ln.pop(0)
                    lt.append([i])                    
        ln.pop()
        return ln==[]

#Runtime: 24 ms, faster than 94.34% of Python3 online submissions for Long Pressed Name.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Long Pressed Name.
#Fu-Ti, Hsu 
#shifty049@gmail.com