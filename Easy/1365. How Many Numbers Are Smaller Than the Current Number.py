class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        a=sorted(nums)
        result=[]
        for i in nums:
            result.append(a.index(i)) 
            
        return result


#Runtime: 132 ms, faster than 45.08% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
#Fu-Ti, Hsu 
#shifty049@gmail.com