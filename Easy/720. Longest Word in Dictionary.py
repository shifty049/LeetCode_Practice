class Solution:
    def longestWord(self, words: List[str]) -> str:        
        l=[]
		#sort by length desc and lexicographical order
        words.sort(key=lambda x:(-1*len(x),x))
        for i in words:
            flag=len(set([i[:j] for j in range(1,len(i),1)])-set(words))==0
			if flag:
				#return the fist solution => the first one has maximal length and the highest lexicographical order
                return i       
        #no solution
		return ''

#Runtime: 72 ms, faster than 88.96% of Python3 online submissions for Longest Word in Dictionary.
#Memory Usage: 14 MB, less than 50.00% of Python3 online submissions for Longest Word in Dictionary.
#Fu-Ti, Hsu 
#shifty049@gmail.com