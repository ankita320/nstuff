class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx2=len(heights)-1
        idx1=0
        maxArea = 0
        while idx1 != idx2:
            curr = abs(idx1-idx2)*min(heights[idx1],heights[idx2])
            if curr > maxArea:
                maxArea = curr
            if heights[idx1] > heights[idx2]:
                idx2-=1
            elif heights[idx1] < heights[idx2]:
                idx1+=1

            elif heights[idx1] == heights[idx2]:
                idx1+=1
        
        return maxArea
                
            


        return maxArea


        