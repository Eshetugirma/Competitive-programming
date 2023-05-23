class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = defaultdict()
        rank = defaultdict()
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        def union(x,y):
            repx = find(x)
            repy = find(y)
            if repx == repy: return 
            if rank[repx] > rank[repy]:
                parent[repy] = repx
            elif rank[repx] < rank[repy]:
                parent[repx] = repy
            else:
                parent[repx] = repy
                rank[repy] += 1
        for i in range(len(stones)):
            parent[i] = i
            rank[i] = 1
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i == j: continue
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        count = 0
        print(parent)
        for i in parent:
            if parent[i] == i:
                count += 1
        return len(stones) - count