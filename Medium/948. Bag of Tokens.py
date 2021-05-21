class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        if not tokens or min(tokens) > power:
            return 0
        
        tokens.sort()
        score = 0
        
        while tokens:
            
            if power > tokens[0]:
                
                power -= tokens.pop(0)
                
                score += 1
                
            else:
                if len(tokens) >= 2:
                    
                    score -= 1
                    power += tokens.pop(-1)
                
                else:
                    if power >= tokens[0]:
                        
                        score += 1
                    
                    break
                        
        return score

#Runtime: 52 ms, faster than 76.82% of Python3 online submissions for Bag of Tokens.
#Memory Usage: 14.4 MB, less than 40.34% of Python3 online submissions for Bag of Tokens.
#Fu-Ti, Hsu 
#shifty049@gmail.com