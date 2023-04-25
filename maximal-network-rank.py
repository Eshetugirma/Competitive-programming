class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(set)
        count = defaultdict(int)
        for i in range(len(roads)):
            dic[roads[i][0]].add(roads[i][1])
            dic[roads[i][1]].add(roads[i][0])
            count[roads[i][0]] += 1
            count[roads[i][1]] += 1
        print(count)
        max1 = float("-inf")
        for key in range(n):
            for key2 in range(n):
                if key == key2:
                    continue
                if key in dic[key2] or key2 in dic[key]:
                    max1 = max(max1, count[key] + count[key2]-1)
                else:
                    max1 = max(max1, count[key]+count[key2])
        return max1