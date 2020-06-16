class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        L=[]
        sumer=sum([i if not i%2 else 0 for i in A])
        for i in queries:           
            if not A[i[1]]%2:
                sumer-=A[i[1]]
            A[i[1]]+=i[0]
            if not A[i[1]]%2:
                sumer+=A[i[1]]                
            L.append(sumer)
        return L

#Runtime: 544 ms, faster than 86.31% of Python3 online submissions for Sum of Even Numbers After Queries.
#Memory Usage: 19.7 MB, less than 5.88% of Python3 online submissions for Sum of Even Numbers After Queries.
#Fu-Ti, Hsu 
#shifty049@gmail.com     