class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by their difference 
        costs = sorted(costs,key=lambda x: abs(x[0]-x[1]),reverse = True)
        n,min_sum,a,b = len(costs)//2,0,0,0

        for cost in costs:
            if a < n and  cost[0] < cost[1] or b >= n:
                min_sum += cost[0]
                a += 1
            else:
                min_sum += cost[1]
                b += 1

        return min_sum