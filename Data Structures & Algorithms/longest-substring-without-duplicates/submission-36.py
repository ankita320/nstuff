class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxi = 0
        d = {}
        left = 0

        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= left:
                left = d[s[i]] + 1

            d[s[i]] = i
            maxi = max(maxi, i - left + 1)

        return maxi