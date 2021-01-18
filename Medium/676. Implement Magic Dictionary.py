class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.magic = []
    def buildDict(self, dictionary: List[str]) -> None:
        
        self.dict = dictionary

    def search(self, searchWord: str) -> bool:
        if searchWord in self.magic:
            return True
        
        for i in self.dict: 
            if searchWord != i and len(searchWord) == len(i):
                if sum([i[jx] == searchWord[jx] for jx in range(len(i))]) == len(i) - 1:
                        self.magic.append(searchWord)
                        return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

#Runtime: 440 ms, faster than 14.65% of Python3 online submissions for Implement Magic Dictionary.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Implement Magic Dictionary.
#Fu-Ti, Hsu 
#shifty049@gmail.com
