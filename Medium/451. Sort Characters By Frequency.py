class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic={}
        for i in set(s):            
            if s.count(i) not in dic:
                dic[s.count(i)]=[i]
            else:
                dic[s.count(i)].append(i)
                
        return ''.join([j*i for i in sorted(dic.keys())[::-1] for j in dic[i]])

#Runtime: 48 ms, faster than 63.14% of Python3 online submissions for Sort Characters By Frequency.
#Memory Usage: 14.8 MB, less than 96.33% of Python3 online submissions for Sort Characters By Frequency.
#Fu-Ti, Hsu 
#shifty049@gmail.com