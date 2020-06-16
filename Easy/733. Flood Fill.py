class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        color= image[sr][sc]
        def dfs(img,idx_r,idx_c):
            
            if idx_r<0 or idx_r>len(image)-1 or idx_c<0 or idx_c>len(image[0])-1 or image[idx_r][idx_c]!=color or image[idx_r][idx_c] == newColor:
                return
            img[idx_r][idx_c]=newColor
            
            dfs(img,idx_r,idx_c+1)
            dfs(img,idx_r,idx_c-1)
            dfs(img,idx_r+1,idx_c)
            dfs(img,idx_r-1,idx_c)
            
        dfs(image,sr,sc) 
        return image
#Runtime: 76 ms, faster than 82.74% of Python3 online submissions for Flood Fill.
#Memory Usage: 14.1 MB, less than 5.56% of Python3 online submissions for Flood Fill.
#Fu-Ti, Hsu 
#shifty049@gmail.com