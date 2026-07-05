class Solution:
    def validPalindrome(self, s: str) -> bool:
        fix = s.lower().replace(" ", "")
        start = 0
        end = len(fix) - 1

        def isPal(l, r):
            while l < r:
                if fix[l] != fix[r]:
                    return False
                l += 1
                r -= 1
            return True

        while start < end:
            if fix[start] != fix[end]:
                return isPal(start + 1, end) or isPal(start, end - 1)
            start += 1
            end -= 1

        return True