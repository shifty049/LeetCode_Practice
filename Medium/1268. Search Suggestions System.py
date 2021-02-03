class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        ans = [[] for _ in range(len(searchWord))]
        
        part = sorted(products)
        for ix,i in enumerate(searchWord):
            
            part = [i for i in part if i[:ix+1] == searchWord[:ix+1]]
            
            if part:
                ans[ix] = part[:3]
            
            else: 
                break
        
        return ans

#Runtime: 84 ms, faster than 81.06% of Python3 online submissions for Search Suggestions System.
#Memory Usage: 17 MB, less than 88.23% of Python3 online submissions for Search Suggestions System.
#Fu-Ti, Hsu 
#shifty049@gmail.com