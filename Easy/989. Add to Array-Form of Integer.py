class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        ath=len(A)-1
        remain=0
        for ix,i in enumerate(list(str(K))[::-1]):
            jx=ix
            ath=len(A)-1
            if ath-jx<0:
                A.insert(0,int(i))    
                
            while ath-jx>=0:
                og=A[ath-jx]
                if jx==ix:
                    A[ath-jx]= (og+int(i)+remain)%10
                    remain=(og+int(i)+remain)//10
                else:
                    A[ath-jx]= (og+remain)%10
                    remain=(og+remain)//10
                
                if remain==0:
                    break                
                if ath-jx==0 and remain!=0:
                    A.insert(0,remain)  
                    remain=0
                    
                jx+=1            
                
        return A

#Runtime: 280 ms, faster than 95.26% of Python3 online submissions for Add to Array-Form of Integer.
#Memory Usage: 14.5 MB, less than 5.00% of Python3 online submissions for Add to Array-Form of Integer.
#Fu-Ti, Hsu 
#shifty049@gmail.com
