import string
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            
            return []
        all_letter = string.ascii_lowercase
        
        dic= {}
        index = 0
        for i in range(2,10):
            num = 3 if i not in [7,9] else 4
            
            dic[str(i)] = list(all_letter[index:index+num])
            index += num
            
        l = dic[digits[0]]
        
        for i in digits[1:]:
            new_l = []
            for wd in l:
                for  j in dic[i]:
                    new_l.append(wd+j)
            l = new_l
        
        return l

#Runtime: 28 ms, faster than 86.01% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 14.3 MB, less than 35.65% of Python3 online submissions for Letter Combinations of a Phone Number.
#Fu-Ti, Hsu 
#shifty049@gmail.com