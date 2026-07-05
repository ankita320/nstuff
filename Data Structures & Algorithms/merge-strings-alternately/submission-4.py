class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        mg = ""
        while p1 < len(word1) and p2 < len(word2):
            mg += word1[p1]
            mg += word2[p2]
            p1+=1
            p2+=1

        if len(word2) < len(word1):
            mg += word1[p1:]

        else:
            mg += word2[p2:]
        
        return mg