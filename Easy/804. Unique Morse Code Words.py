class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        q=[]
        for i in words:
            s=''
            for j in i:
                s+=l[ord(j)-97]
            q.append(s)
        return len(set(q))

#Runtime: 32 ms, faster than 89.70% of Python3 online submissions for Unique Morse Code Words.
#Memory Usage: 13.8 MB, less than 49.21% of Python3 online submissions for Unique Morse Code Words.
#Fu-Ti, Hsu 
#shifty049@gmail.com