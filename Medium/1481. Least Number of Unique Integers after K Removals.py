class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dic  = {}
        for i in arr:
            
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        key_lst = collections.deque(sorted(dic.values(), key = lambda x: -x))
        
        
        while k:
            
            if key_lst[-1] <= k:
                
                k -= key_lst[-1]
                
                key_lst.pop()
            
            else:
                
                k = 0
        
        return len(key_lst)

#Runtime: 428 ms, faster than 91.10% of Python3 online submissions for Least Number of Unique Integers after K Removals.
#Memory Usage: 31 MB, less than 83.95% of Python3 online submissions for Least Number of Unique Integers after K Removals.#Fu-Ti, Hsu 
#Fu-Ti, Hsu 
#shifty049@gmail.com