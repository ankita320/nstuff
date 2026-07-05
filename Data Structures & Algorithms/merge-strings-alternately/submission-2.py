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

        while p1 < len(word1):
            mg += word1[p1]
            p1+=1

        while p2 < len(word2):
            mg += word2[p2]
            p2+=1
        
        return mg