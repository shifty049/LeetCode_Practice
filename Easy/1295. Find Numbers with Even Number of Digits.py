class Solution:
    def findNumbers(self, nums: List[int]) -> int:        
        def check(t):
            n=0
            while t:
                t//=10
                n+=1
            return 0 if n%2 else 1        
        return sum([check(i) for i in nums])

#Runtime: 52 ms, faster than 80.41% of Python3 online submissions for Find Numbers with Even Number of Digits.
#Memory Usage: 13.8 MB, less than 74.63% of Python3 online submissions for Find Numbers with Even Number of Digits.
#Fu-Ti, Hsu 
#shifty049@gmail.com