class Solution:
    def minFlips(self, target: str) -> int:
    
        count = 0
        check = target[:: -1]
        for ix, i in enumerate(check):      
            if not ix or i != check[ix - 1]:
                count += 1
        
        if check[-1] == '0':
            count -= 1
        return count

#Runtime: 94 ms, faster than 60.78% of Python3 online submissions for Minimum Suffix Flips.
#Memory Usage: 14.7 MB, less than 69.12% of Python3 online submissions for Minimum Suffix Flips.
#Fu-Ti, Hsu 
#shifty049@gmail.com