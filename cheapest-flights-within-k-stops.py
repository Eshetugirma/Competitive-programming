class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        le = len(flights)
        graph = defaultdict(list)
        costs = defaultdict() 
        for (x,y,price) in flights: 
            graph[x].append(y) 
            costs[(x,y)] = price  
        

        heap = [(0,src,k)]
        seen = defaultdict()
        while heap:
            curr_cost,curr_node,k = heappop(heap) 
            seen[curr_node] = curr_cost
            # print(heap)
            if curr_node == dst: return curr_cost
            if k >= 0:          
                for child in graph[curr_node]: 
                    child_cost = curr_cost+costs[(curr_node,child)]
                    if le > 14 and child in seen and seen[child] <= child_cost : continue 
                    heappush(heap,(child_cost,child,k-1))
                
            k -= 1
        return -1