class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #two points, one at start and one at end
        #compare s and e -> if equal && abs(s-e) <= k -> true
        #if not equal: check two more nested conditions
        #if s and e -1 are equal
        #if not
            #if s + 1 and e are equal
            #if not, s+1, e-1
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False