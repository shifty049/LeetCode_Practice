class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:        
        L=[]        
        for i in range(len(points)):
            dic={}
            for j in range(len(points)):                
                if i!=j:
                    #d=distance
                    d=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2   
                    if d not in  dic:                       
                        dic[d]=[points[j]]
                    else:                        
                        for k in dic[d]:
                            # append two for each combonation
                            L.append([points[i],k,points[j]])
                            L.append([points[i],points[j],k])
                        
                        dic[d].append(points[j])
        return len(L)

#Runtime: 1216 ms, faster than 61.50% of Python3 online submissions for Number of Boomerangs.
#Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Number of Boomerangs.
#Fu-Ti, Hsu 
#shifty049@gmail.com  