class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        l= []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1

        if 0 in d:
            for i in range(d[0]):
                nums[i] = 0

        
        if 1 in d:
            count1=d[0] if 0 in d else 0
            for i in range(d[1]):
                nums[count1] = 1
                count1+=1

        if 2 in d:
            count2=d.get(0,0)+d.get(1,0)
            for i in range(d[2]):
                nums[count2] = 2
                count2+=1


        
        return nums
        

        