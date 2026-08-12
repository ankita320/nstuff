class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                mn = nums[i]
                count+=1
                break
        if count == 0:
            return nums[0]

        return mn

        