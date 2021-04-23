class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        if '(' not in s:
            return s
        
        check = list(s)
    
        stack = []
        idx = 0
        while idx < len(check):

            if check[idx] == '(':

                stack.append(idx)

            elif check[idx] == ')':

                start = stack.pop()
                check[start:idx+1] = [''] + check[start+1:idx][::-1] + ['']

            idx += 1

        return ''.join(check)

#Runtime: 28 ms, faster than 81.22% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
#Memory Usage: 14.1 MB, less than 95.22% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
#Fu-Ti, Hsu 
#shifty049@gmail.com