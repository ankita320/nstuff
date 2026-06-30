class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #s, e
        #while s < e
        #move s fwd or e bwd
        #max counter
        #f-p < max -> move s by 1
        #f-p > max -> e back by 1
        s = 0
        e = 1
        maxCount = 0
        while e < len(prices):
            if prices[e]<prices[s]:
                s=e
            else:
                if maxCount < prices[e]-prices[s]:
                    maxCount = prices[e]-prices[s]
            e+=1
            
        return maxCount

        