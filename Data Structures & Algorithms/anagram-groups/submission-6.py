class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = []
        f= {}
        fin = []
        for i in strs:
            s.append("".join(sorted(i)))

        
        for i in range(len(strs)):
            if s[i] not in f:
                f[s[i]] = [strs[i]]
            else:
                f[s[i]].append(strs[i])

        for i in f:
            fin.append(f[i])

        return fin
