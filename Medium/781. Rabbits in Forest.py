class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        dic = {}
        
        for i in answers:
            
            if i not in dic:
                dic[i] = 1
            
            else:
                dic[i] += 1
        
        return sum([(i+1)*(j//(i+1)+ int(j%(i+1)!=0)) if i!=0 else j for i,j in dic.items()])

#Runtime: 40 ms, faster than 83.20% of Python3 online submissions for Rabbits in Forest.
#Memory Usage: 14.4 MB, less than 59.60% of Python3 online submissions for Rabbits in Forest.
#Fu-Ti, Hsu 
#shifty049@gmail.com
