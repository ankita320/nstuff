class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        e = 1
        maxCount = 0

        while e < len(prices):
            if prices[e] < prices[s]:
                s = e
            else:
                maxCount = max(maxCount, prices[e] - prices[s])

            e += 1

        return maxCount