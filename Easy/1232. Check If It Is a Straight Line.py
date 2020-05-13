class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates)==2:
            return True
          
        ix=2
        ratio=[(coordinates[1][1]-coordinates[0][1]),(coordinates[1][0]-coordinates[0][0])]
        while (coordinates[ix][1]-coordinates[ix-1][1])*ratio[1]==(coordinates[ix][0]-coordinates[ix-1][0])*ratio[0]:
                        
            if ix==len(coordinates)-1:
                return True
                
            ix+=1
        return False
#Runtime: 56 ms, faster than 91.64% of Python3 online submissions for Check If It Is a Straight Line.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Check If It Is a Straight Line.
#Fu-Ti, Hsu 
#shifty049@gmail.com