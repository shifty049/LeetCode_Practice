class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max = 0
        def helper(dic, st):
            if st == len(s):
                # print('nums: ', dic)
                self.max = max(self.max, len(dic))
            else:                
                for ix in range(st + 1 , len(s) + 1):
                    check = s[st : ix]
                    if check not in dic:
                        
                        dict_copy = dict(dic)
                        dict_copy[check] = True
                        helper(dict_copy, ix)

        helper({}, 0)
        
        return self.max

#Runtime: 344 ms, faster than 61.04% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
#Memory Usage: 14.2 MB, less than 60.71% of Python3 online submissions for Split a String Into the Max Number of Unique Substrings.
#Fu-Ti, Hsu 
#shifty049@gmail.com