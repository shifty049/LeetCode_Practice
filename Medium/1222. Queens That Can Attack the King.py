class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        L=[]
        ix=king[0]
        jx=king[1]
        
        if [i for i in queens if i[1]==jx and i[0]>ix]:
            L.append(sorted([i for i in queens if i[1]==jx and i[0]>ix])[0])
        if [i for i in queens if i[1]==jx and i[0]<ix]:
            L.append(sorted([i for i in queens if i[1]==jx and i[0]<ix])[-1])
        if [i for i in queens if i[0]==ix and i[1]>jx]:
            L.append(sorted([i for i in queens if i[0]==ix and i[1]>jx])[0])
        if [i for i in queens if i[0]==ix and i[1]<jx]:
            L.append(sorted([i for i in queens if i[0]==ix and i[1]<jx])[-1])
        
        if [i for i in queens if i[1]-jx==i[0]-ix and i[1]>jx]:
            L.append(sorted([i for i in queens if i[1]-jx==i[0]-ix and i[1]>jx])[0])
        if [i for i in queens if i[1]-jx==i[0]-ix and i[1]<jx]:
            L.append(sorted([i for i in queens if i[1]-jx==i[0]-ix and i[1]<jx])[-1])
        if [i for i in queens if i[1]-jx==ix-i[0] and i[1]>jx]:
            L.append(sorted([i for i in queens if i[1]-jx==ix-i[0] and i[1]>jx])[-1])
        if  [i for i in queens if i[1]-jx==ix-i[0] and i[1]<jx]:
            L.append(sorted([i for i in queens if i[1]-jx==ix-i[0] and i[1]<jx])[0])          
        return L
#Runtime: 40 ms, faster than 61.71% of Python3 online submissions for Queens That Can Attack the King.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Queens That Can Attack the King.
#Fu-Ti, Hsu 
#shifty049@gmail.com