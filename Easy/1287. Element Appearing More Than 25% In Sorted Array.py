class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        ix=0
        while len(arr):
            if arr[ix] not in dic:
                dic[arr[ix]]=1
            else:
                dic[arr[ix]]+=1
             
            if dic[arr[ix]]> len(arr)//4:
                return arr[ix]
            ix+=1

#Runtime: 92 ms, faster than 83.51% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
#Memory Usage: 15.1 MB, less than 59.22% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com