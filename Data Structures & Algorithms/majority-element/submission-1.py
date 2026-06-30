class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxNum = 0
        idx=0
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        
        for i in freq:
            if freq[i]>maxNum:
                maxNum = freq[i]
                idx=i
        
        return idx
        