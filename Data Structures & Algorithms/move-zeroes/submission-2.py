class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx1 = 0
        idx2 = 1
        while idx1 < len(nums)-1 and idx2 < len(nums):
            if nums[idx1] == 0 and nums[idx2] > 0:
                tmp = nums[idx1]
                nums[idx1] = nums[idx2]
                nums[idx2] = tmp
                idx1 += 1
                idx2 += 1
            elif nums[idx1] == 0 and nums[idx2] == 0:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1

        return nums
