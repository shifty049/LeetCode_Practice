class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        dic = {} 
        ans = 0
       
        for ix,i in enumerate(nums[:-1]):
            for jx in range(ix+1,len(nums)):
                
                product = nums[ix] * nums[jx]
                
                if product not in dic:
                    dic[product] = 1
                else:
                    dic[product] += 1
                    
        for product, value in dic.items():
            
            if dic[product] > 1:
               
                ans += 4 * (value * (value - 1)) 
                    
        return ans

# Runtime: 536 ms, faster than 92.32% of Python3 online submissions for Tuple with Same Product.
# Memory Usage: 42.8 MB, less than 99.59% of Python3 online submissions for Tuple with Same Product.
#Fu-Ti, Hsu 
#shifty049@gmail.com