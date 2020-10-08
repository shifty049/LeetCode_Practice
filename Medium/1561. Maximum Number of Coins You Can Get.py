 class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        
        piles.sort()
        
        new_pile = piles[len(piles)//3:]
        return sum([new_pile[ix] for ix,i in  enumerate(new_pile) if not ix%2 ])

#Runtime: 592 ms, faster than 99.72% of Python3 online submissions for Maximum Number of Coins You Can Get.
#Memory Usage: 26.3 MB, less than 27.84% of Python3 online submissions for Maximum Number of Coins You Can Get.
#Fu-Ti, Hsu 
#shifty049@gmail.com