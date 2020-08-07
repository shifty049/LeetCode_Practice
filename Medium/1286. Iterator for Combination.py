class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):        
        self.l=[]
        def dfs(nums,res):           
            if len(res)==combinationLength:
                if res not in self.l:
                    self.l.append(res)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:],res+[nums[i]])
        dfs(list(characters),[])

    def next(self) -> str:
        return ''.join(self.l.pop(0))

    def hasNext(self) -> bool:
        return self.l

#Runtime: 688 ms, faster than 5.26% of Python3 online submissions for Iterator for Combination.
#Memory Usage: 16.1 MB, less than 39.86% of Python3 online submissions for Iterator for Combination.
#Fu-Ti, Hsu 
#shifty049@gmail.com