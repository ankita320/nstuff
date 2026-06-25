class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Stores seen numbers as keys and their indices as values
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the required partner number was already processed
            if complement in seen:
                return [seen[complement], index]
                
            # Store the current number and index if its complement isn't found yet
            seen[num] = index
            
        return []  # Return empty if no solution exists