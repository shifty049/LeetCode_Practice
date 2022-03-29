class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        lst = list(answerKey)
        maxer = 0       
        dic = dict()
        queue = collections.deque()
        
        for ix, i in enumerate(lst):
            queue.append(i)

            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

            while 'T' in dic and 'F' in dic and min(dic.values()) > k:
                
                rv = queue.popleft()
                dic[rv] -= 1

                if not dic[rv]:
                    del dic[rv]
                    break

            maxer = max(maxer, sum(dic.values()))

        return maxer

#Runtime: 628 ms, faster than 50.12% of Python3 online submissions for Maximize the Confusion of an Exam.
#Memory Usage: 15 MB, less than 8.44% of Python3 online submissions for Maximize the Confusion of an Exam.
#Fu-Ti, Hsu 
#shifty049@gmail.com