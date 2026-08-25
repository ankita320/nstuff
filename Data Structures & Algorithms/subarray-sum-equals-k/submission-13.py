class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #ex: 2 -1 1 2
        #count
        #start at l -> keep going if as adding r -> < k
        #if nums[l] = k, move l up, mark it in count
        # once == k, move l up by 1, subtract nums[l] from sum, r+=1
        count = 0
        curr_sum = 0
        freq = {0:1}

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in freq:
                count+=freq[curr_sum-k]

            if curr_sum in freq:
                freq[curr_sum]+=1
            else:
                freq[curr_sum] = 1
            
        return count
        