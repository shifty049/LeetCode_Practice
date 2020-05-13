class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        a='0'
        b=str(n)
        while '0' in a or '0' in b:
            a=str(int(a)+1)
            b=str(int(n)-int(a))
        
        return [a,b]

#Runtime: 20 ms, faster than 97.93% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
#Fu-Ti, Hsu 
#shifty049@gmail.com