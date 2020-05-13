class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        return list(map(lambda x: x+extraCandies>=max(candies),candies))

#Runtime: 36 ms, faster than 91.46% of Python3 online submissions for Kids With the Greatest Number of Candies.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Kids With the Greatest Number of Candies.
#Fu-Ti, Hsu 
#shifty049@gmail.com