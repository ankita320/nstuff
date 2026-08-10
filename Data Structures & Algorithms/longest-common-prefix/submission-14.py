class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        length = []
        for i in range(len(strs)):
            length.append(len(strs[i]))

        acc = len(strs)
        num = 1
        pre = 0

        for i in range(min(length)):
            num = 1
            for j in range(1,len(strs)):
                if strs[j][i] == strs[j-1][i]:
                    num +=1
            if num == acc:
                pre+=1
            else:
                break
            
        
        if pre > 0:
            return strs[0][0:pre]
        else:
            return ""






            

            