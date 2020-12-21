class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        
        st_row = 0
        st_col = 0
        start_direct_index = 0
        direct = ['right','down','left', 'up']
        
        Spiral = [[None] * n for _ in range(n)]
        
        for i in range(1,n**2+1):
            Spiral[st_row][st_col] = i
            if i == n**2:
                break
            
            if direct[start_direct_index] == 'right':
                
                if st_col < n-1 and Spiral[st_row][st_col+1]== None:
                    st_col+=1
                else: start_direct_index = (start_direct_index+1)%4
                    
            
            if direct[start_direct_index] == 'down':
                if st_row < n-1 and Spiral[st_row+1][st_col]== None:
                    st_row+=1
                else: start_direct_index = (start_direct_index+1)%4
            
            if direct[start_direct_index] == 'left':
                if st_col > 0 and Spiral[st_row][st_col-1]== None:
                    st_col-=1
                else: start_direct_index = (start_direct_index+1)%4
            
            if direct[start_direct_index] == 'up':
                if st_row > 0 and Spiral[st_row-1][st_col]== None:
                    st_row-=1
                else: 
                    start_direct_index = (start_direct_index+1)%4
                    
                    if st_col < n-1 and Spiral[st_row][st_col+1]== None:
                        st_col+=1
                    else: start_direct_index = (start_direct_index+1)%4
        
        return Spiral

#Runtime: 32 ms, faster than 74.53% of Python3 online submissions for Spiral Matrix II.
#Memory Usage: 14.3 MB, less than 60.31% of Python3 online submissions for Spiral Matrix II.
#Fu-Ti, Hsu 
#shifty049@gmail.com