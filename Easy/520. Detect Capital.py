class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word)==1:
            return True
        
        if word[0]==word[0].upper():
            h=U
        else:
            h=L
        if h==U:
            
            return word[1:] in [word[1:].upper(),word[1:].lower()]
        else:
            return word[1:]==word[1:].lower()

#Runtime: 16 ms, faster than 99.82% of Python3 online submissions for Detect Capital.
#Memory Usage: 13.7 MB, less than 6.67% of Python3 online submissions for Detect Capital.
#Fu-Ti, Hsu 
#shifty049@gmail.com