class Solution:
    def reverseWords(self, s: str) -> str:
        
        a=''
        for i in s.split(' '):
            
            a+=''.join(str(i)[::-1])+' '
            
        return a.rstrip()

#Runtime: 28 ms, faster than 89.84% of Python3 online submissions for Reverse Words in a String III.
#Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
#Fu-Ti, Hsu 
#shifty049@gmail.com