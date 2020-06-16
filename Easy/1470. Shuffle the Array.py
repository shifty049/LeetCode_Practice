class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        l=[]       
        for i in range(n):
            l+=[nums[i],nums[n+i]]
        return l

#Runtime: 56 ms, faster than 96.29% of Python3 online submissions for Shuffle the Array.
#Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com