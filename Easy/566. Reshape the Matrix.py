class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:       
        # not able to reshape so return original matrix
        if r*c!=len(nums)*len(nums[0]):
            return nums       
        origin=[i for j in nums for i in j]
        L=[]
        for i in range(0,len(origin),c):            
            L.append(origin[i:i+c])        
        return L

#Runtime: 100 ms, faster than 82.22% of Python3 online submissions for Reshape the Matrix.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reshape the Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com

        