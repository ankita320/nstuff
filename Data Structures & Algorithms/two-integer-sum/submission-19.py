class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Stores seen numbers as keys and their indices as values
        freq = {}
        for i, num in enumerate(nums):
            com = target - num
            if com in freq:
                return [freq[com],i]
            
            freq[num] = i

        return []
            
