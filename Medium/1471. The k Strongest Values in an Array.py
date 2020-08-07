class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        arr.sort()
        m=arr[(len(arr)-1)//2]        
        return [i[1] for i in sorted(([[abs(i-m),i] for i in arr]))[::-1]][:k]

#Runtime: 1164 ms, faster than 80.28% of Python3 online submissions for The k Strongest Values in an Array.
#Memory Usage: 33.9 MB, less than 100.00% of Python3 online submissions for The k Strongest Values in an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com