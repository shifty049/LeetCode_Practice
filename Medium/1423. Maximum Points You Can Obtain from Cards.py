class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])
        
        maxer = sum(cardPoints[:k])
        starter = maxer
        start_index = k - 1
        while start_index  >= 0:
            starter = starter -cardPoints[start_index] + cardPoints[start_index - k]
            if starter > maxer:
                maxer = starter
            start_index -= 1
        
        return maxer

#Runtime: 396 ms, faster than 94.48% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
#Memory Usage: 27.7 MB, less than 36.19% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
#Fu-Ti, Hsu 
#shifty049@gmail.com