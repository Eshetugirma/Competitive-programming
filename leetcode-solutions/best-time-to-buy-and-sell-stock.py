class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)-1
        max_profit = 0
        max_sell = 0
        for i in range(n,-1,-1):
            max_sell = max(max_sell,prices[i])
            max_profit = max(max_profit,max_sell - prices[i])
        return max_profit

