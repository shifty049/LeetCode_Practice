class Solution:
    def addDigits(self, num: int) -> int:
        
        while len(str(num))>1:
            num=sum([int(i) for i in str(num)])           
        return num

#Runtime: 28 ms, faster than 80.21% of Python3 online submissions for Add Digits.
#Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Add Digits.
#Fu-Ti, Hsu 
#shifty049@gmail.com