class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        dic={}
        for ix,i in enumerate(points):         
            if i[0]**2+i[1]**2 not in dic:
                dic[i[0]**2+i[1]**2]=[ix]
            else:
                 dic[i[0]**2+i[1]**2].append(ix)
               
        return [points[j] for i in sorted(dic.keys()) for j in dic[i]][:K]

#Runtime: 808 ms, faster than 34.13% of Python3 online submissions for K Closest Points to Origin.
#Memory Usage: 19.2 MB, less than 67.15% of Python3 online submissions for K Closest Points to Origin.
#Fu-Ti, Hsu 
#shifty049@gmail.com