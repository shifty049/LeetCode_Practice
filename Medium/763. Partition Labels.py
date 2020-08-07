class Solution:
    def partitionLabels(self, S: str) -> List[int]:        
        lst=[]
        for i in S:             
            lst.append(i)
            idx=0
            while idx <len(lst)-1:
                if i in lst[idx]:
                    lst=lst[:idx]+[''.join(lst[idx:])]
                    break
                idx+=1
        return list(map(lambda x:len(x),lst))

#Runtime: 72 ms, faster than 11.97% of Python3 online submissions for Partition Labels.
#Memory Usage: 13.8 MB, less than 65.72% of Python3 online submissions for Partition Labels.
#Fu-Ti, Hsu 
#shifty049@gmail.com
