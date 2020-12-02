class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.max_length = 0
        def backtracking(lst, string):
            
            if len(set(string)) == len(string):
                self.max_length = max(len(string), self.max_length) 
            
            else:
                return self.max_length
         
            
            for ix,i in enumerate(lst):
                backtracking(lst[ix+1:], string+i)
            
            return self.max_length
        
        return backtracking(arr, '')
                
#Runtime: 108 ms, faster than 57.33% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
#Memory Usage: 14.3 MB, less than 54.48% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
#Fu-Ti, Hsu 
#shifty049@gmail.com