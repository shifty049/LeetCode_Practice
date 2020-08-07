class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        if N<2:
            return int(N==0)
        s=''
        while N:
            N,R=divmod(N,2)
            
            s=str(int(int(R)==0))+s
        q=0        
        for ix,i in enumerate(s):
            q+=int(i)*2**(len(s)-ix-1)
        return q

#Runtime: 20 ms, faster than 98.90% of Python3 online submissions for Complement of Base 10 Integer.
#Memory Usage: 13.8 MB, less than 64.75% of Python3 online submissions for Complement of Base 10 Integer.
#Fu-Ti, Hsu 
#shifty049@gmail.com