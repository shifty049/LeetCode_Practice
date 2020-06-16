class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:        
        maxer=0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    res=[points[i],points[j],points[k]]
                    area=0.5 * abs(res[0][0] * (res[1][1] - res[2][1]) + res[1][0] * (res[2][1] - res[0][1]) + res[2][0] * (res[0][1] - res[1][1]))
                    maxer= maxer if maxer>= area else area          
        return maxer
#Runtime: 168 ms, faster than 50.35% of Python3 online submissions for Largest Triangle Area.
#Memory Usage: 13.9 MB, less than 12.50% of Python3 online submissions for Largest Triangle Area.
#Fu-Ti, Hsu 
#shifty049@gmail.com
