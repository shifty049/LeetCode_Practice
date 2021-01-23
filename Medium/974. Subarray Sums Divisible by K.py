class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        dic = {0:1}
        
        count = 0
        
        sumer = 0
        
        for i in A:
            
            sumer += i         
               
            remain = sumer % K
                
            if remain in dic:
                count += dic[remain]
        
            if remain not in dic:
                dic[remain] = 1
            else:
                dic[remain] += 1
            
        return count

#Runtime: 292 ms, faster than 85.78% of Python3 online submissions for Subarray Sums Divisible by K.
#Memory Usage: 18.3 MB, less than 73.58% of Python3 online submissions for Subarray Sums Divisible by K.
#Fu-Ti, Hsu 
#shifty049@gmail.com
