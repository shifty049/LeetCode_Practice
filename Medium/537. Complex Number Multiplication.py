class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        
        ax,ay = int(a.split('+')[0]),int(a.split('+')[-1][:-1])
        bx,by = int(b.split('+')[0]),int(b.split('+')[-1][:-1])
        
        return '{}+{}i'.format(ax*bx - ay*by, ax*by+ay*bx)

#Runtime: 24 ms, faster than 93.83% of Python3 online submissions for Complex Number Multiplication.
#Memory Usage: 13.8 MB, less than 57.84% of Python3 online submissions for Complex Number Multiplication.
#Fu-Ti, Hsu 
#shifty049@gmail.com