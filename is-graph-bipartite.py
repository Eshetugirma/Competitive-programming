class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0]*len(graph)
 
        # dfs iteratively 
        for i in range(len(graph)):
            if not color[i]:
                color[i] = 1
                stack = [i]
                while stack:
                    curr = stack.pop()
                    for child in graph[curr]:
                        if color[child]:
                            if color[child] == color[curr]: return False
                        else:
                            color[child] = - color[curr]
                            stack.append(child)

        return True