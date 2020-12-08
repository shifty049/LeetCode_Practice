class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
            
        queue = {'0000'}
        level = 0
        path = set()
        while queue:
           
            if target in queue:
                return level
            
            for item in queue:
                path.add(item)
    
            new_queue = set()
            for item in queue:
                
                if item not in deadends:
                    
                    for jx,j in enumerate(item):
                        
                        for rotate in [1, -1]:
                            str_list = list(item)
                            str_list[jx] = str((int(j) + 10 + rotate )%10)
                            new_num = ''.join(str_list)
                            if new_num not in path:
                                new_queue.add(new_num)
            queue = new_queue
            level+=1
        return -1

#Runtime: 1136 ms, faster than 24.65% of Python3 online submissions for Open the Lock.
#Memory Usage: 15.7 MB, less than 13.67% of Python3 online submissions for Open the Lock.
#Fu-Ti, Hsu 
#shifty049@gmail.com
