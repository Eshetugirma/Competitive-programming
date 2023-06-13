class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        connection = defaultdict(list)
        #===>>>> here we can simply construct graph or generate connections
        for i in range(len(prerequisites)):
            connection[prerequisites[i][1]].append(prerequisites[i][0])
        #==>>> this is bfs function to find if there is such prerequisite in connection
        def bfs(que,u,v):
            que.append(v)
            visited = set()
            while que:
                v = que.popleft()
                if v == u: return True
                for curr in connection[v]:
                    if curr not in visited:
                        que.append(curr)
                        visited.add(curr)
            return False
        #==>>> this it to check and record every given queries
        ans = []
        for u,v in queries:
            ans.append(bfs(deque(),u,v))
        return ans