class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sumer = 0
        ans = inf
        queue = collections.deque()
        for i in nums:
            
            sumer += i
            queue.append(i)
            
            if sumer == target:
                
                if len(queue) < ans:
                    ans = len(queue)
            else:
                while sumer > target:
                             
                    minus = queue.popleft()
                    if sumer - minus >= target:
                        sumer -= minus
                        if sumer == target:
                            if len(queue) < ans:
                                ans = len(queue)
                            break
        
                    else:
                        queue.insert(0, minus)
                        if len(queue) < ans:
                            ans = len(queue)            
                        break                 
        return ans if ans != inf else 0

#Runtime: 80 ms, faster than 83.13% of Python3 online submissions for Minimum Size Subarray Sum.
#Memory Usage: 16.9 MB, less than 13.39% of Python3 online submissions for Minimum Size Subarray Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com