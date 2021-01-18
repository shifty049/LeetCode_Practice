class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        sl = []
        ans = []
        
        pl =[0]*26
        for i in p:
            pl[ord(i)-97]+=1
        
        for ix, i in enumerate(s):
            if not sl:            
                sl = [0]*26         
                for i in s[:len(p)]:
                    sl[ord(i)-97] +=1
                
            else:
                if ix+len(p)-1 < len(s):
                    sl[ord(s[ix-1])-97]-=1
                    sl[ord(s[ix+len(p)-1])-97]+=1
                else:
                    return ans
            if sl == pl:
                ans.append(ix)
        return ans

#Runtime: 112 ms, faster than 76.82% of Python3 online submissions for Find All Anagrams in a String.
#Memory Usage: 15.3 MB, less than 35.40% of Python3 online submissions for Find All Anagrams in a String.
#Fu-Ti, Hsu 
#shifty049@gmail.com