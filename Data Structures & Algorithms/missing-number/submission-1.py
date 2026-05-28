class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = {}
        f = 0
        for i in range(len(nums)+1):
            n[i] = 0
            if i in nums:
                n[i] += 1
        
        for i in n:
            if n[i] == 0:
                f = i
        return f
                