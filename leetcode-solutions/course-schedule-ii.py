class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list) 
        in_degree = defaultdict(int) 
        for i,j in prerequisites:
            graph[i].append(j)
            in_degree[j] += 1
        que = deque()
        ans = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                que.append(i)
                ans.append(i)
        while que:
            for i in range(len(que)):
                currCourse = que.popleft()
                for nextCourse in graph[currCourse]:
                    in_degree[nextCourse] -= 1
                    if in_degree[nextCourse] == 0:
                        que.append(nextCourse)
                        ans.append(nextCourse)
        ans.reverse()
        return ans if len(ans) == numCourses else []

        