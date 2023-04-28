class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs) == 1: return 1
        ans = 0
        def culc(point1,point2):
            x = abs(point1[0] - point2[0])
            y = abs(point1[1] - point2[1])
            return 1 if point1[2] >= pow(x**2+y**2,0.5) else 0



        #==>>> construct the graph
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j: 
                    if culc(bombs[i],bombs[j]):
                        graph[i] += [j]
        

        #===>>> the function which work dfs
        def dfs(index,visited):
            for ind in graph[index]:
                if ind not in visited:
                    visited.add(ind)
                    dfs(ind,visited) 
            return visited

        #==>>>> for every bomb try the maximum they can explore
        for i in range(len(bombs)):
            visited = dfs(i,set([i]))
            ans = max(ans,len(visited))
        return ans