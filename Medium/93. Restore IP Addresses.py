class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        lst = []
        length = len(s)
        def backtracking(num, count, sub_lst):
            if len(sub_lst)>1 and (int(s[sub_lst[-2]:sub_lst[-1]]) > 255 or (s[sub_lst[-2]] == '0' and len(s[sub_lst[-2]:sub_lst[-1]])>1)):
                return
            if num >= length or count >= 4:
                if count == 4 and  num==length:
                    if sub_lst not in lst:
                        lst.append('.'.join([s[i:sub_lst[ix+1]] for ix,i in enumerate(sub_lst[:-1])]))
                
                return
            
            for i in range(1, length - num - 2 + count ):
                backtracking(num+i, count+1, sub_lst+[sub_lst[-1]+i])
        
        backtracking(0 , 0, [0])
        return lst

#Runtime: 148 ms, faster than 8.99% of Python3 online submissions for Restore IP Addresses.
#Memory Usage: 14.4 MB, less than 7.55% of Python3 online submissions for Restore IP Addresses.
#Fu-Ti, Hsu 
#shifty049@gmail.com