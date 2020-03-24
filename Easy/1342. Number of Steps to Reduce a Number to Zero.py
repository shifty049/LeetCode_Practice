class Solution:
    def numberOfSteps (self, num: int) -> int:
        step=0
        while num!=0:
            
            # for even => divided by 2
            if num%2==0:
                num=num/2
            # for odd => minus 1
            else:
                num-=1
                
            step+=1
        # return number of steps
        return step

#Runtime: 24 ms, faster than 86.66% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
#Fu-Ti, Hsu 
#shifty049@gmail.com