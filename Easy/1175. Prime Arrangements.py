class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        np=1
        p=0
        for i in range(2,n+1):
            
            is_np=False
            
            for j in range(2,i):
                
                if  not i%j:
                    np+=1
                    is_np=True
                    break
            if not is_np:
                p+=1  
        def dfs(n):
            if n in [0,1]:
                return 1
            return dfs(n-1)*n
        return dfs(np)*dfs(p)%(10**(9)+7)

#Runtime: 24 ms, faster than 94.72% of Python3 online submissions for Prime Arrangements.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Prime Arrangements.
#Fu-Ti, Hsu 
#shifty049@gmail.com