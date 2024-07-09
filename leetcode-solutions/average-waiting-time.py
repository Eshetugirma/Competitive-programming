class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        total = 0
        for a,w in customers:
            total += w
            if wait > a:
                total += wait - a 
            wait = max(a,wait) + w
        return total/len(customers)