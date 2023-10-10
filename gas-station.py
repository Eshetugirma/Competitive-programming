class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        circular_cost = cost + cost
        circular_gas = gas + gas
        # print(circular_gas)
        start = 0
        while start < n:
            if gas[start] >= cost[start]:
                cost_sum = 0
                gas_sum = 0
                
                for i in range(start,n+start):
                    # print(i,cost_sum,gas_sum)
                    cost_sum += circular_cost[i]
                    gas_sum += circular_gas[i]
                    if cost_sum > gas_sum:
                        start = i
                        break
                if i - start +1 == n: return start
                    
            start += 1
        return -1