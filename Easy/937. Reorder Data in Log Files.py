class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dic={}
        l=[]
        for  i in logs:            
            if not i.split(' ')[1][0].isdigit():
                if ' '.join(i.split(' ')[1:]) not in dic:    
                   
                    dic[' '.join(i.split(' ')[1:])]=[i]
                else:
                    dic[' '.join(i.split(' ')[1:])].append(i)
            else:     
                l.append(i)
                
                      
        for i in sorted(dic.keys())[::-1]:
            l=sorted(dic[i])+l
        return l

#Runtime: 32 ms, faster than 90.85% of Python3 online submissions for Reorder Data in Log Files.
#Memory Usage: 14.1 MB, less than 5.02% of Python3 online submissions for Reorder Data in Log Files.
#Fu-Ti, Hsu 
#shifty049@gmail.com