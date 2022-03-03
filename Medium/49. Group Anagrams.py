import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        
        dic = collections.defaultdict(list)      
        for st in strs:
            origin = [0] * 26
            
            for char in st:
                origin[ord(char) - ord('a')] += 1
           
            dic[tuple(origin)].append(st)
        
        return list(dic.values())

#Runtime: 112 ms, faster than 79.63% of Python3 online submissions for Group Anagrams.
#Memory Usage: 19 MB, less than 27.35% of Python3 online submissions for Group Anagrams.
#Fu-Ti, Hsu 
#shifty049@gmail.com
