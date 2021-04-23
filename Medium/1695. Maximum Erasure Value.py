class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        ans = {}
        
        max_sumer = 0
        start = 0
        sumer = 0
        for ix,i in enumerate(nums):
            # print(i, sumer)
            if i not in ans:
                
                ans[i] = i
                sumer += i
            else:
                
                while nums[start] != nums[ix]:
                    
                    del ans[nums[start]]
                    sumer -= nums[start]
                    start += 1
              
                start += 1
                
            if sumer > max_sumer:
                max_sumer = sumer 

        return max(max_sumer, sum(ans.values()))

#Runtime: 1116 ms, faster than 97.62% of Python3 online submissions for Maximum Erasure Value.
#Memory Usage: 28.2 MB, less than 62.57% of Python3 online submissions for Maximum Erasure Value.
#Fu-Ti, Hsu 
#shifty049@gmail.com