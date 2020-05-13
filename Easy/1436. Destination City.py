class Solution:
    def destCity(self, paths: List[List[str]]) -> str:            
        ix=0
        lst=[i[0] for i in  paths]
        while  paths[ix][1] in lst:
                ix=lst.index(paths[ix][1])             
        return  paths[ix][1]
#Runtime: 48 ms, faster than 98.49% of Python3 online submissions for Destination City.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Destination City.
#Fu-Ti, Hsu 
#shifty049@gmail.com