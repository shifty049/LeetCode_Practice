class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        
        while pushed:
            
            if not stack or popped[0] != stack[-1]:
                stack.append(pushed.pop(0))
            while popped and stack and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()
        
        return not stack

#Runtime: 68 ms, faster than 84.50% of Python3 online submissions for Validate Stack Sequences.
#Memory Usage: 14.5 MB, less than 62.30% of Python3 online submissions for Validate Stack Sequences.
#Fu-Ti, Hsu 
#shifty049@gmail.com