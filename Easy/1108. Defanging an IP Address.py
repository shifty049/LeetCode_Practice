class Solution:
    def defangIPaddr(self, address: str) -> str:
        qx=0
        a=list(address)
        for ix, i in enumerate(a):
            if i=='.':
                qx+=1
                a[ix]='[.]'
            # already replace in all three nodes
            if qx==3:
                return ''.join(a)

#Runtime: 20 ms, faster than 96.27% of Python3 online submissions for Defanging an IP Address.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
#Fu-Ti, Hsu 
#shifty049@gmail.com