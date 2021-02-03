class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        
        dic = {0:1}
        sum = 0
        ans = 0
        
        for i in A:
            sum += i
           
            if sum - S in dic:
                ans += dic[sum - S] 
            
            if i:
                dic[sum] = 1
            
            else:
                dic[sum] += 1
        
        return ans

#Runtime: 240 ms, faster than 96.81% of Python3 online submissions for Binary Subarrays With Sum.
#Memory Usage: 17.6 MB, less than 43.90% of Python3 online submissions for Binary Subarrays With Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com