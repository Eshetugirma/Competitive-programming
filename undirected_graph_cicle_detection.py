from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    graph = defaultdict(list)
	    parents = [-1]*V
	    visited = [False]*V
	    for i in range(len(adj)):
	        graph[i] = adj[i]
	    def bfs(que):
	        visited[i] = True
	        while que:
	            temp = que.pop()
	            for el in adj[temp]:
	                if not visited[el]:
	                    visited[el] = True
	                    que.append(el)
	                    parents[el] = temp
	                elif el != parents[temp]:
	                     return 1
	        return 0
	    for i in range(V):
	        if not visited[i] and bfs([i]):
    	           return 1
	    return 0
	    