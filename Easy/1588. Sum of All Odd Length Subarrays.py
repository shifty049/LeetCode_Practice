class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        sumer = 0
        
        for i in range(1, len(arr)+1, 2):
            
            for j in range(len(arr)+1-i):
                
                sumer+= sum(arr[j:j+i])
        
        return sumer

#Runtime: 64 ms, faster than 58.68% of Python3 online submissions for Sum of All Odd Length Subarrays.
#Memory Usage: 14.3 MB, less than 20.25% of Python3 online submissions for Sum of All Odd Length Subarrays.
#Fu-Ti, Hsu 
#shifty049@gmail.com
