class Solution:
    def maximumSwap(self, num: int) -> int:
        
        maxer = num
        num = list(str(num))
        for i in range(len(num) -1):
            if num[i+1] > num[i]:
                break
        else:
            return maxer
        
        for ix in range(i+1):
            for jx in range(i+1,len(num)):                
                s= num[:]        
                if s[ix] < s[jx]:
                    s[ix],s[jx] = s[jx],s[ix]

                    if int(''.join(s)) > maxer:
                        maxer = int(''.join(s))
        return maxer

#Runtime: 20 ms, faster than 99.46% of Python3 online submissions for Maximum Swap.
#Memory Usage: 14.3 MB, less than 61.30% of Python3 online submissions for Maximum Swap.
#Fu-Ti, Hsu 
#shifty049@gmail.com