class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        grid = [[False]*numCourses for i in range(numCourses)]
        for i,j in prerequisites:
            grid[i][j] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    grid[i][j] = grid[i][j] or (grid[i][k] and grid[k][j])
        ans = []
        # print(grid)
        for i,j in queries:
            ans.append(grid[i][j])
        return ans