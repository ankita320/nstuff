class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxi =0
        track_l = []

        while r < len(prices):
            if (prices[r]-prices[l] < maxi):
                if prices[l] > prices[r]:
                    l = r

            else:
                maxi = max(maxi, prices[r]-prices[l])
            r+=1

        return maxi




