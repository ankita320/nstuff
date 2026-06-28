class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        uni = 0
        while r < len(nums):
            if nums[l] >= nums[r]:
                r+=1
            else:
                uni+=1
                tmp = nums[l+1]
                nums[l+1]=nums[r]
                nums[r]=tmp
                l+=1
                r=l+1
                
        return uni+1
            # 1 2 1 3 4
            
        