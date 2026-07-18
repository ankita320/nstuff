class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        prodNoZero = 1
        numZeros = 0

        for i in nums:
            if i == 0:
                numZeros+=1
        
        if numZeros > 1:
            for i in nums:
                output.append(0)
            return output

        
        for i in nums:
            if i == 0:
                prodNoZero *= 1
                prod *= i
            else:
                prod *= i
                prodNoZero *= i
        
        for i in nums:
            if i == 0:
                output.append(prodNoZero)
            else:
                output.append(prod//i)
        
        return output
        