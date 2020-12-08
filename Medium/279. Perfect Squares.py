class Solution:
    def numSquares(self, n: int) -> int:
            
        level = 0
        solution_set = {n}
        
        while True:
            level+=1
            
            new_solution_set  = set()
            
            for item in solution_set:
                for minus_item in range(int(n**0.5),0,-1):

                    rest = item - minus_item**2
                    if not rest:
                        return level

                    new_solution_set.add(rest)

            solution_set = new_solution_set

#Runtime: 672 ms, faster than 73.03% of Python3 online submissions for Perfect Squares.
#Memory Usage: 15.8 MB, less than 17.45% of Python3 online submissions for Perfect Squares.
#Fu-Ti, Hsu 
#shifty049@gmail.com