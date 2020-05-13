class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        rk=1
        miner=None
        dic={}
        for i in sorted(set(arr)):
            if miner==None:
                miner=i            
            if i==miner:
                dic[i]=rk
            else:
                miner=i
                rk+=1
                dic[i]=rk
                
        return [dic[i] for i in arr]

#Runtime: 364 ms, faster than 76.45% of Python3 online submissions for Rank Transform of an Array.
#Memory Usage: 34.6 MB, less than 100.00% of Python3 online submissions for Rank Transform of an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com