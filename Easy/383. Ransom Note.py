class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for i in set(ransomNote):
            
            if i not in magazine:
                return False
            
            if magazine.count(i)<ransomNote.count(i):
                return False
        
        return True

#Runtime: 32 ms, faster than 94.78% of Python3 online submissions for Ransom Note.
#Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Ransom Note.
#Fu-Ti, Hsu 
#shifty049@gmail.com