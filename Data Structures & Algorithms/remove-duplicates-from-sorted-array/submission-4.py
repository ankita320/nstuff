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
            
        l = 0
        r = 1
        uniq = 1
        while l < len(nums) and r < len(nums):
            if nums[l] == nums[r]:
                r+=1
                l+=1
            if nums[l] < nums[r]:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                r +=1
                l = r-1
                uniq+=1

        

        