class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        counter=0
        k={}
        #find out total passenger after counting enterance and exit in each location during this trip
        for i in trips:
            if i[1] not in k.keys():
                k[i[1]]=i[0]
            else:
                k[i[1]]+=i[0]
            if i[2] not in k.keys():
                k[i[2]]=i[0]*-1
            else:
                k[i[2]]-=i[0]
        #check if number of total passengers is over capicity in any location during this trip
        for i in sorted(k.keys()):
            
            counter+=k[i]
            
            if counter>capacity:
                return False
        return True

#Runtime: 64 ms, faster than 61.68% of Python3 online submissions for Car Pooling.
#Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Car Pooling.
#Fu-Ti, Hsu 
#shifty049@gmail.com
        