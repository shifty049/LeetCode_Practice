class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        s=''
        remain=0
        num1,num2=(max(len(num1),len(num2))-len(num1))*'0'+num1,(max(len(num1),len(num2))-len(num2))*'0'+num2
        for i in range(len(num1)-1,-1,-1):
            
            s,remain=str((int(num1[i])+int(num2[i])+remain)%10)+s,(int(num1[i])+int(num2[i])+remain)//10
       
        return '1'+s if remain==1 else s

#Runtime: 44 ms, faster than 56.36% of Python3 online submissions for Add Strings.
#Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Add Strings.
#Fu-Ti, Hsu 
#shifty049@gmail.com