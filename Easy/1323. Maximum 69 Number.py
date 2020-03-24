class Solution:
    def maximum69Number (self, num: int) -> int:
        
        # not 6 in this number => already the max
        if '6' not in str(num):
            
            return num
                
        ix=0
        a=list(str(num))
        #replace the first 6 with 9
        while a[ix]!='6':
            ix+=1
              
        a[ix]='9'
        
        return int(''.join(a))

#Runtime: 24 ms, faster than 85.27% of Python3 online submissions for Maximum 69 Number.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Maximum 69 Number.
#Fu-Ti, Hsu 
#shifty049@gmail.com
    
        