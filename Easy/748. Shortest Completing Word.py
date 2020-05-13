class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        dic={}
        
        for i in licensePlate.lower():
            if i.isalpha():
            
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
        
        A=None
        for i in words:
            
            if not A or len(i)<len(A):
                if all([i.count(j)>=dic[j] for j in dic.keys()]):
                    if not A:
                        A=i
                    else: A= i if len(i)<len(A) else A 
        return A
#Runtime: 60 ms, faster than 95.86% of Python3 online submissions for Shortest Completing Word.
#Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Shortest Completing Word.
#Fu-Ti, Hsu 
#shifty049@gmail.com
