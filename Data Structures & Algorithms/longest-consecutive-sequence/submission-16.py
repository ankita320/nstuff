class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort array
        #0,3,2,5,4,6,1,1
        #0 1 1 2 3 4 5 6
       
        # num tracker
        #max tracker 
        #while -> parse through check if its 1 more than i-1 (use index, start at 1) -> if its the same continue
        # not the same and not greater than 1
            #end the count -> store it in max, start l at the first value that diffed
        new = sorted(nums)
        num = 0
        mx = 0
        i = 1
        while i < len(new):
            if new[i] - new[i-1] == 1:
                num+=1
            elif new[i] - new[i-1] == 0:
                num+=0
            else:
                if num > mx:
                    mx = num
                num = 0
            i+=1
        if len(nums) == 0:
            return 0

        else:
            return max(mx,num) + 1
        
        
