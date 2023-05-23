import heapq as h
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
       
        graph = defaultdict(list)
    

        for i in range(len(points)):   
            temp = float('inf')
            for j in range(i+1,len(points)):
                
                curr = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])
                graph[i].append((curr,j))
                graph[j].append((curr,i))



        
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        def union(x,y):
            parent1 = find(x)
            parent2 = find(y)
            if parent1 == parent2: return False
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
            elif rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
            else: 
                parent[parent1] = parent2
                rank[parent2] += 1
            return True

        visited=set({0})

        heap=graph[0]
        h.heapify(heap)

        totalDist=0
        while heap:

            dist,cur=h.heappop(heap)

            if cur not in visited:

            
                visited.add(cur)
                totalDist+=dist
                for nbr in graph[cur]:
                  
                    h.heappush(heap,nbr)
            if len(visited)==len(points):
                return totalDist

        return totalDist