class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 1
        h = x // 2
        ans = 0
        while l <= h:
            mid = (l+h)//2
            if x == (mid*mid):
                return mid
                
            elif x < (mid*mid):
                h = mid - 1
                
            else:
                l = mid + 1
                ans = mid

        return ans


