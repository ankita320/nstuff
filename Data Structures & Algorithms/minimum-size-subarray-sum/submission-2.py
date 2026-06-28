class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        #min keep track of subarray length
        #left and right -> keep moving right until num >= target
        #if => target -> min - right-left+1 IF curr <
            #mv left + 1, right l+1
        l = 0
        r = 0
        curr = 0
        minNum = 9999
        track = 0
        while r < len(nums):
            curr += nums[r]
            if curr < target:
                r+=1
            else:
                track = r-l+1
                if track < minNum:
                    minNum = track
                l+=1
                r=l
                curr = 0
        if minNum == 9999:
            return 0
        else: 
            return minNum


