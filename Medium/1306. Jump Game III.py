class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        
        answer=[None]*len(arr)
            
        self.check=False
        
        def dfs(idx,nums):
                        
            if idx>len(arr)-1 or idx<0:
                return
            if nums[idx]==0:
                self.check=True
                return
            if nums[idx]!=None:
                return
           
            nums[idx]=arr[idx]
            
            for i in [idx+arr[idx],idx-arr[idx]]:
                dfs(i,nums)
        
        dfs(start,answer)
        
        return self.check

#Runtime: 232 ms, faster than 92.11% of Python3 online submissions for Jump Game III.
#Memory Usage: 23.3 MB, less than 100.00% of Python3 online submissions for Jump Game III.
#Fu-Ti, Hsu 
#shifty049@gmail.com