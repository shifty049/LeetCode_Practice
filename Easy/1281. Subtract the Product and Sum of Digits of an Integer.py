class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        s=[]
        while True:
            if n<10:
                s.append(n)
                break
            d,r=divmod(n,10)
            s.append(r)
            n=d
           
        return reduce(lambda x,y:x*y,s)-sum(s)

#Runtime: 16 ms, faster than 99.64% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
#Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
#Fu-Ti, Hsu 
#shifty049@gmail.com