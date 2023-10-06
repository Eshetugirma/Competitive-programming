class Solution: 
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        paths = [0]*(n+1)
        if n > 10:
            m = int(pow(n,0.5))
        else:
            m = n-1
        # print(len(edges)*n)
        paths[start_node] = 1 
        for _ in range(m):
            for i in range(len(edges)):
                paths[edges[i][0]] = max(paths[edges[i][0]],paths[edges[i][1]]*succProb[i])
                paths[edges[i][1]] = max(paths[edges[i][1]],paths[edges[i][0]]*succProb[i])
        # print(paths)
        # print(paths[1])
        return paths[end_node]