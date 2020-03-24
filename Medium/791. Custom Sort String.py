class Solution:
    def customSortString(self, S: str, T: str) -> str:

        q=''
        lt=list(T)
        for i in S:         
            while i in lt:
                q+=i
                lt.remove(i)
                
        return q+''.join(lt)

#Runtime: 32 ms, faster than 27.79% of Python3 online submissions for Custom Sort String.
#Memory Usage: 13 MB, less than 90.00% of Python3 online submissions for Custom Sort String.
#Fu-Ti, Hsu 
#shifty049@gmail.com