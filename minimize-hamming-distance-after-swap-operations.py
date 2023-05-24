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
            parent.setdefault(x,x)
            parent.setdefault(y,y)
            parent[find(x)] = parent[find(y)]
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