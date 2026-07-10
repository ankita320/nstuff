class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        # First window
        curr = 0
        for i in range(k):
            curr += abs(arr[i] - x)

        s = curr
        bestStart = 0

        # Slide the window
        for i in range(k, len(arr)):
            curr += abs(arr[i] - x)          # add new element
            curr -= abs(arr[i-k] - x)        # remove old element

            if curr < s:
                s = curr
                bestStart = i - k + 1

        return arr[bestStart:bestStart+k]