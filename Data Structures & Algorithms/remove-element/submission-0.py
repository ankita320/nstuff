class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track the position of valid elements
        k = 0 
        
        # Iterate through the list with a scanning pointer
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Place it at the index tracked by k
                nums[k] = nums[i]
                # Increment k to the next available position
                k += 1
                
        # Return the total number of non-val elements
        return k