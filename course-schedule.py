class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connect = [[] for i in range(numCourses)]
        print(connect)
        degree = [0]*numCourses
        for i,pairs in prerequisites:
            connect[pairs].append(i)
            degree[i] += 1
        ans = [i for i in range(numCourses) if degree[i] == 0]
        for el in ans:
            for preq in connect[el]:
                degree[preq] -= 1
                if degree[preq] == 0:
                    ans.append(preq)
        return len(ans) == numCourses