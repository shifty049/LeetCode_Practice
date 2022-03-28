class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        presum = 0
        dic = {0 : -1}
        idx = 0
        for i in nums:
            presum += i
            
            retention = presum % k
            
            if retention not in dic:
                dic[retention] = idx
            else:
                if idx - dic[retention] > 1:
                    return True           
            
            idx += 1
        return False

#Runtime: 1091 ms, faster than 62.60% of Python3 online submissions for Continuous Subarray Sum.
#Memory Usage: 33.2 MB, less than 38.51% of Python3 online submissions for Continuous Subarray Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com