class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l=0
        r=0
        curr = 0
        while r < len(s):
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                curr+=1
                r+=1
            else:
                if curr >= maxLength:
                    maxLength = curr
                curr=0
                l+=1
                r=l
        if maxLength > curr:
            return maxLength
        else: 
            return curr
                