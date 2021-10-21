from collections import Counter
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        check = Counter(text)
                
        lst = []
        for i in text:
            if not lst:
                lst.append(i)
            else:
                if i == lst[-1][-1]:
                    lst[-1] += i
                else:
                    lst.append(i)
    
        mx = 0
        for ix,i in enumerate(lst):
            if not ix or ix == len(lst) - 1:
                if len(i) < check[i[0]]:           
                    mx = max(mx, len(i) + 1)
                else:
                    mx = max(mx, len(i))
            else:      
                if len(i) > 1:
                    if len(i) < check[i[0]]:           
                        mx = max(mx, len(i) + 1)
                    else:
                        mx = max(mx, len(i))        
                else:          
                    if lst[ix - 1][-1] == lst[ix + 1][-1]:

                        if  len(lst[ix - 1]) + len(lst[ix + 1]) < check[lst[ix + 1][-1]]:

                            mx = max(mx, len(lst[ix - 1]) + len(lst[ix + 1]) + 1)
                        else:
                            mx = max(mx, len(lst[ix - 1]) + len(lst[ix + 1]))   
           
        return mx

#Runtime: 74 ms, faster than 52.84% of Python3 online submissions for Swap For Longest Repeated Character Substring.
#Memory Usage: 14.8 MB, less than 64.89% of Python3 online submissions for Swap For Longest Repeated Character Substring.
#Fu-Ti, Hsu 
#shifty049@gmail.com