class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result=0
        for i in S:
            if i in J:
                result+=1
        return result


#Runtime: 28 ms, faster than 70.13% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
#Fu-Ti, Hsu 
#shifty049@gmail.com