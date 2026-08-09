class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxA = max(maxA, height * width)

            if i < len(heights):
                stack.append(i)

        return maxA