class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        total = 0
        def dp(index,check):
            if index == len(prices):
                return 0

            buy = 0
            notBuy = 0
            sell = 0
            notSell = 0
            if (index,check) in memo:
                return memo[(index,check)]
            
            if check:
                

                buy = dp(index+1,False) - prices[index]
                notBuy = dp(index+1,True)

                currency = max(buy, notBuy)

            else:
                sell = dp(index+1,True) + prices[index] - fee
                notSell = dp(index+1,False)

                currency  = max(sell, notSell)
            memo[(index, check)] = currency
            return memo[(index, check)]

        return dp(0,True)