class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        lst=[0]*num_people
        idx=0
        cds=1
        while candies:
            if candies>cds:         
                lst[idx]+=cds
                candies-=cds
                cds+=1
                idx=(idx+1)%len(lst)
            
            else:
                lst[idx]+=candies
                break
        
        return lst

#Runtime: 44 ms, faster than 50.78% of Python3 online submissions for Distribute Candies to People.
#Memory Usage: 13.7 MB, less than 96.59% of Python3 online submissions for Distribute Candies to People.
#Fu-Ti, Hsu 
#shifty049@gmail.com