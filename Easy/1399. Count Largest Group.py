class Solution:
    def countLargestGroup(self, n: int) -> int:
        l=[0]*37
        for j in range(1,n+1): 
            ans=0
            while True:
                j,remain=divmod(j,10)
                ans+=remain                
                if j<10:
                    ans+=j
                    break
            l[ans]+=1       
        return len([i for i in l if i==max(l)])

#Runtime: 88 ms, faster than 87.51% of Python3 online submissions for Count Largest Group.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Count Largest Group.
#Fu-Ti, Hsu 
#shifty049@gmail.com