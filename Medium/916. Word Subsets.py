class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:        
        L=[]
        dic={}        
        for i in B:
            for letter in i:                
                if letter not in dic.keys():
                    dic[letter]=i.count(letter)
               
                elif i.count(letter)>dic[letter]:
                    dic[letter]=i.count(letter)
        for i in A:          
            check=True
            for k,v in dic.items():
                
                if k not in i or i.count(k)<v:
                    check=False
                    break                
            if check:
                L.append(i)
                    
        return L

#Runtime: 516 ms, faster than 96.32% of Python3 online submissions for Word Subsets.
#Memory Usage: 17.5 MB, less than 50.00% of Python3 online submissions for Word Subsets.
#Fu-Ti, Hsu 
#shifty049@gmail.com
