class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        check = self.dict
        
        for wd in key:
            
            if wd not in check:
                check[wd] = {'value': {key:val}}
            
            else:
                check[wd]['value'].update({key:val})
            
            check = check[wd]
        

    def sum(self, prefix: str) -> int:
        
        check = self.dict
        for i in prefix:
            
            if i not in check:
                return 0
            
            check = check[i]
        
        return sum(check['value'].values())


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

#Runtime: 28 ms, faster than 89.76% of Python3 online submissions for Map Sum Pairs.
#Memory Usage: 14.3 MB, less than 54.53% of Python3 online submissions for Map Sum Pairs.
#Fu-Ti, Hsu 
#shifty049@gmail.com