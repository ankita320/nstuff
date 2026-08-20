class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if target > nums[len(nums)-1]:
            return len(nums)
        elif target < nums[0]:
            return 0

        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid -1
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        return l

        