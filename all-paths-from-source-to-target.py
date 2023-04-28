class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(temp, curr):
            temp.append(curr) 
            if curr == len(graph)-1:
                ans.append(temp)
                return  
            for i in graph[curr]:
                dfs(temp[::],i)
        for curr in graph[0]:
            dfs([0],curr)
        return ans