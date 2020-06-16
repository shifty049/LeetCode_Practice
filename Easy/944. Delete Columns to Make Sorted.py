class Solution:
    def minDeletionSize(self, A: List[str]) -> int:        
        count=0
        for i in list(zip(*A)):
            if list(i)!=sorted(i):
                count+=1
        return count

#Runtime: 96 ms, faster than 89.74% of Python3 online submissions for Delete Columns to Make Sorted.
#Memory Usage: 14.6 MB, less than 8.33% of Python3 online submissions for Delete Columns to Make Sorted.
#Fu-Ti, Hsu 
#shifty049@gmail.com