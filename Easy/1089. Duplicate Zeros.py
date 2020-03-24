class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        q=list(arr)
        idx=0
        for ix,i in enumerate(q):
            if i==0:
                loc=ix+idx
                # insert postion plus one after one insert
                arr.insert(loc,0)
                # deleteing one goes by inserting one to keep arr length unchanged
                arr.pop()
                idx+=1

#Runtime: 64 ms, faster than 95.58% of Python3 online submissions for Duplicate Zeros.
#Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
#Fu-Ti, Hsu 
#shifty049@gmail.com               