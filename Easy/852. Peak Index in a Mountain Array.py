class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:       
        for i in range(1,len(A)-1):           
            if A[i]>A[i-1] and A[i]>A[i+1]:               
                return i

#Runtime: 76 ms, faster than 82.29% of Python3 online submissions for Peak Index in a Mountain Array.
#Memory Usage: 14.2 MB, less than 63.64% of Python3 online submissions for Peak Index in a Mountain Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com               