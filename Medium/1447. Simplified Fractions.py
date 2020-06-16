class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        l=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if j==1:
                    l.append('%s/%s'%(j,i))
                else:
                    a=int(i)
                    b=int(j)
                    while b:
                        a,b=b,a%b
                    if a==1:
                        l.append('%s/%s'%(j,i))
        return l
#Runtime: 216 ms, faster than 83.52% of Python3 online submissions for Simplified Fractions.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Simplified Fractions.
#Fu-Ti, Hsu 
#shifty049@gmail.com