class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.mapping = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
         
            if key not in self.dict:
                self.dict[key] = {}
                self.mapping[key] = []
            self.dict[key][timestamp] = value
            self.mapping[key].append(timestamp)
   
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dict:
           
            return ''
        
        check_timestamp = self.mapping[key]
        
        if timestamp < check_timestamp[0]:
            return ''
        
        elif timestamp == check_timestamp[0]:
            return self.dict[key][check_timestamp[0]]
        
        elif timestamp >= check_timestamp[-1]:
            return self.dict[key][check_timestamp[-1]]
                
        left,right = 0 , len(check_timestamp)
         
        while  right - left >1:
            
            mid = (left+right)//2
        
            if check_timestamp[mid] > timestamp:
                right =  mid
            elif check_timestamp[mid] < timestamp:
                left =  mid
            else:
                return self.dict[key][check_timestamp[mid]]
        
        return self.dict[key][check_timestamp[left]]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#Runtime: 596 ms, faster than 99.23% of Python3 online submissions for Time Based Key-Value Store.
#Memory Usage: 69 MB, less than 86.37% of Python3 online submissions for Time Based Key-Value Store.
#Fu-Ti, Hsu 
#shifty049@gmail.com