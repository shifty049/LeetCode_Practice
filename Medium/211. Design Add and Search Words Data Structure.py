class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        
    def addWord(self, word: str) -> None:
        
        check = self.dic
        
        for i in word:
            
            if i not in check:
                check[i] = {}
            
            check = check[i]
        
        check['exist']  = True
        
    def search(self, word: str) -> bool:
        
        if not self.dic:
            return False
        
        check = [self.dic]
        
        for i in word:
            
            if check:
                new_check = []
        
                for ck in check:
                    if i!= '.':

                        if i in ck:
                            new_check.append(ck[i])

                    else:
                        for j in ck:
                            if j!= 'exist':
                                new_check.append(ck[j])
                check = new_check
            
            if not check:
                return False
        
        for dic in check:
            
            if 'exist' in dic:
           
                return True
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

#Runtime: 220 ms, faster than 89.69% of Python3 online submissions for Design Add and Search Words Data Structure.
#Memory Usage: 24.8 MB, less than 73.64% of Python3 online submissions for Design Add and Search Words Data Structure.
#Fu-Ti, Hsu 
#shifty049@gmail.com