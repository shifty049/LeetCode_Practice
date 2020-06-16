class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:           
        ix=0
        dic={5:0,10:0,20:0}
        while ix<len(bills):   
            
            if bills[ix]==5:
                dic[bills[ix]]+=1
            elif bills[ix]==10:
                dic[5]-=1
                if dic[5]<0:
                    return False
                dic[bills[ix]]+=1           
            else:
                if dic[10]>0:
                    dic[10]-=1
                    dic[5]-=1
                else:
                     dic[5]-=3  
                
                if dic[5]<0:
                    return False
                dic[bills[ix]]+=1
            ix+=1
        return True

#Runtime: 140 ms, faster than 89.39% of Python3 online submissions for Lemonade Change.
#Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for Lemonade Change.
#Fu-Ti, Hsu 
#shifty049@gmail.com