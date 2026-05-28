class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        if s==t:
            return True;
        
        s_d = {}
        t_d = {}
        for i,j in zip(s,t):
            if i not in s_d:
                s_d[i] = 1
            else:
                s_d[i] += 1
            if j not in t_d:
                t_d[j] = 1
            else:
                t_d[j] += 1
        return s_d==t_d 
        