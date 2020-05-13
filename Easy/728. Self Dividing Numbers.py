class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]: 
        l=[]
        for i in range(left,right+1):
            ck,rm=divmod(i,10)     
            check=True
            while ck>=0:
                if ck==rm==0:
                    break
                if not rm or i%rm:
                    check=False
                    break
                ck,rm=divmod(ck,10)
            if check:
                l.append(i)           
        return l

#Runtime: 40 ms, faster than 91.02% of Python3 online submissions for Self Dividing Numbers.
#Memory Usage: 13.7 MB, less than 8.00% of Python3 online submissions for Self Dividing Numbers.
#Fu-Ti, Hsu 
#shifty049@gmail.com
