class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = defaultdict()
        rank = defaultdict()
        #===>>>> here is find function
        def find(x):
            parent.setdefault(x,x)
            if x == parent[x]:
                return parent[x]
            return find(parent[x])
        #===>>> this is the union function
        def union(x,y):
            parent1 = find(x)
            parent2 = find(y)
            if parent1 == parent2: return
            if rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
            elif rank[parent1] < rank[parent2]:
                parent[parent2] = parent1
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
        #===>>> define parent by them selfs and give rank of one for all index allowed
        for pair in allowedSwaps:
            parent[pair[0]] = pair[0]
            parent[pair[1]] = pair[1]
            rank[pair[0]] = 1
            rank[pair[1]] = 1
        #==>>>> here i call my union function to connect 
        for pair in allowedSwaps:
            union(pair[0],pair[1])
        temp = defaultdict(dict)
        #===>>> collect the swaps we can applies 
        for i,val in enumerate(source):
            temp[find(i)].setdefault(val,0)
            temp[find(i)][val] += 1
        ans = 0
        for i,val in enumerate(target):
            if val in temp[find(i)]:
                temp[find(i)][val] -= 1
                if not temp[find(i)][val]:
                    del temp[find(i)][val]
            else:
                ans += 1
        return ans