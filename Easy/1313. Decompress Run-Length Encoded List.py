class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        L=[]
        # select by per two elements for value and frequency
        for i in range(0,len(nums),2):
            L+=[nums[i+1]]*nums[i]
            
        return L

#Runtime: 64 ms, faster than 87.52% of Python3 online submissions for Decompress Run-Length Encoded List.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.
#Fu-Ti, Hsu 
#shifty049@gmail.com