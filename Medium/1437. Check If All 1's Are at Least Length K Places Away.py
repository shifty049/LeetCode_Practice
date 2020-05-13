class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:       
        st=0        
        while st<len(nums):            
            if not nums[st]:
                st+=1            
            else:
                check=0
                st+=1
                while st <len(nums) and not nums[st]:
                    st+=1
                    check+=1                                      
                if check<k and st <len(nums) and nums[st]:
                    return False
        return True

#Runtime: 596 ms, faster than 86.11% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
#Memory Usage: 17.2 MB, less than 100.00% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
#Fu-Ti, Hsu 
#shifty049@gmail.com