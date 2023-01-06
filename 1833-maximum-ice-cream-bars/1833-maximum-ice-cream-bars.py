class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        buckets = [0] * (max(costs)+1)
        for p in costs:
            buckets[p] += 1
        
        res = 0
        for price, count in enumerate(buckets):
            if coins < price:
                break
            if count > 0:
                res += min(count, coins//price)
                coins -= min(coins, price * count)
        return res