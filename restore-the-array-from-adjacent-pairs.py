class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        connections = defaultdict(list)
        for pair in adjacentPairs:
            connections[pair[0]].append(pair[1])
            connections[pair[1]].append(pair[0])


        def dfs(prev,visited):
            for curr in connections[prev]:
                if curr not in visited:
                    ans.append(curr)
                    visited.add(curr)
                    dfs(curr,visited)

                    
        ans = []
        for k,v in connections.items():
            if len(v)==1:
                ans.append(k)
                dfs(k,{k})
                return ans