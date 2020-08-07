class Solution:
    def findLucky(self, arr: List[int]) -> int:        
        dic={i : 0 for i in set(arr)}       
        for i in arr: 
            if i in dic:
                dic[i]+=1               
                if dic[i]>i:
                    del dic[i]            
        return max([i for i in dic if i==dic[i]]) if [i for i in dic if i==dic[i]] else -1

#Runtime: 52 ms, faster than 92.33% of Python3 online submissions for Find Lucky Integer in an Array.
#Memory Usage: 13.9 MB, less than 28.07% of Python3 online submissions for Find Lucky Integer in an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com