class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        left = 0
        right = 0
        #==>>> iterate prices and find best max in every itaretion 
        while right < len(prices):
            #==>>> if you see prices less than before update as ur buying day
            if prices[left] > prices[right]:
                left = right
            #==>> then find all possible maxprofit by selling every day after u buy
            maxp = max(maxp,prices[right]-prices[left])
            right += 1
        return maxp
                