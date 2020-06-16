class Solution:
    def reverseOnlyLetters(self, S: str) -> str:     
        dicl={}
        dicnl={}
        for ix,i in enumerate(S):
            if ord(i) in list(range(65,91))+list(range(97,123)):
                dicl[ix]=i
            else:
                dicnl[ix]=i
        
        diclr={i:list(dicl.values())[::-1][ix] for ix,i in enumerate(dicl)}        
        z = {**diclr, **dicnl}
        return ''.join(z[i] for i in sorted(z))

#Runtime: 28 ms, faster than 75.87% of Python3 online submissions for Reverse Only Letters.
#Memory Usage: 14 MB, less than 5.56% of Python3 online submissions for Reverse Only Letters.
#Fu-Ti, Hsu 
#shifty049@gmail.com