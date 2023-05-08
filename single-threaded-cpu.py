class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key= lambda x:x[0])
        heap = []
        ans = []
        i = 0
        time = tasks[0][0]
        while len(ans) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time :
                heappush(heap,(tasks[i][1],tasks[i][2]))
                i += 1
            if heap:
                temp = heappop(heap)
                ans.append(temp[1])
                time += temp[0]
            elif i < len(tasks):
                time = tasks[i][0]
        return ans