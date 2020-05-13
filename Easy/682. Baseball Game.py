class Solution:
    def calPoints(self, ops):
        v=[]
        sumer=0
        for i in ops:           
            if i not in ['C','D','+']:
                sumer+=int(i)
                v.append(int(i))            
            elif i=='C':
                if v:
                    sumer-=v.pop()            
            elif i=='D':
                if v:
                    pt=v[-1]*2
                    sumer+=pt
                    v.append(pt)
            else:
                if v:
                    pt=sum(v[-2:])    
                    sumer+=pt
                    v.append(pt)
        return sumer

#Runtime: 36 ms, faster than 83.31% of Python3 online submissions for Baseball Game.
#Memory Usage: 14.2 MB, less than 10.00% of Python3 online submissions for Baseball Game.
#Fu-Ti, Hsu 
#shifty049@gmail.com