class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        self.l=list(range(len(rooms)))
        def dfs(ix):
            if ix not in self.l or not self.l:
                return
            self.l.remove(ix)
            for index in rooms[ix]:
                dfs(index)
        dfs(0)
        return not self.l

#Runtime: 76 ms, faster than 23.31% of Python3 online submissions for Keys and Rooms.
#Memory Usage: 14.4 MB, less than 9.09% of Python3 online submissions for Keys and Rooms.
#Fu-Ti, Hsu 
#shifty049@gmail.com