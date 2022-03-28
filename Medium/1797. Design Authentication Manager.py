class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.dic = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        
        if tokenId in self.dic:
            if self.dic[tokenId] > currentTime:
                self.dic[tokenId] = currentTime + self.timeToLive
            else:
                del self.dic[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        new_dic = {}
        for key, val in self.dic.items():
            if val > currentTime:
                new_dic[key] = val
        
        self.dic = new_dic
        return len(self.dic)
            
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

#Runtime: 284 ms, faster than 65.75% of Python3 online submissions for Design Authentication Manager.
#Memory Usage: 15.5 MB, less than 91.78% of Python3 online submissions for Design Authentication Manager.
#Fu-Ti, Hsu 
#shifty049@gmail.com
