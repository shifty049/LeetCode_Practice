class Solution:
    def binaryGap(self, N: int) -> int:
        
        dic={'1':None}
        mx=0
        for ix,i in enumerate(bin(N)):
            if i=='1':
                if not dic['1']:
                    
                    dic['1']=ix
                else:
                    mx=max(mx,ix-dic['1'])
                    dic['1']=ix        
        return mx

#Runtime: 20 ms, faster than 96.59% of Python3 online submissions for Binary Gap.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Gap.
#Fu-Ti, Hsu 
#shifty049@gmail.com