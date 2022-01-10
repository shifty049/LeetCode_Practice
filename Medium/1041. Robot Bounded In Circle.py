class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
                
        direct = {0:[0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}
        pre_dir_index = cur_dir_index = 0
        path = 0
        check = set()
        rounds = 0
        loc = [0, 0]
        while True and rounds < 4:
            for ix, i in enumerate(instructions):

                if i == 'G':
                    loc[0] += direct[cur_dir_index][0]
                    loc[1] += direct[cur_dir_index][1]

                elif i == 'L':
                    cur_dir_index = (cur_dir_index - 1) % 4

                else:
                    cur_dir_index = (cur_dir_index + 1) % 4
            
            if loc == [0, 0]:
                return True
            
            if cur_dir_index == pre_dir_index or cur_dir_index in check:                 
                return False

            check.add(cur_dir_index)
            
            pre_dir_index = cur_dir_index
            rounds += 1
            
        return True

#Runtime: 28 ms, faster than 86.38% of Python3 online submissions for Robot Bounded In Circle.
#Memory Usage: 14.3 MB, less than 15.50% of Python3 online submissions for Robot Bounded In Circle.
#Fu-Ti, Hsu 
#shifty049@gmail.com