class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def calculateDistance(x,y,x1,y1):
            return ((x-x1)**2+(y-y1)**2)**0.5
        def bfs(i):
            que = deque([i])
            temp_seen = set([i])
            count = 1
            while que:
                n = len(que)
                for i in range(n):
                    curr = que.popleft() 
                    for neighbor in graph[curr]:

                        if neighbor not in temp_seen:
                            que.append(neighbor)
                            seen.add(neighbor)
                            temp_seen.add(neighbor)

            
            return len(temp_seen)

        graph = {i:[] for i in range(len(bombs))}

        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                dist = calculateDistance(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1])
                if bombs[i][2] >= dist:
                    graph[i].append(j)
                if bombs[j][2] >= dist:
                    graph[j].append(i)

        seen = set()
        globalMaxima = 1

        for i in range(len(bombs)):
            if i not in seen:
                seen.add(i)
                currDetonate = bfs(i)
                globalMaxima = max(globalMaxima,currDetonate)
                # print(globalMaxima,seen,currDetonate,i)
        return globalMaxima



        