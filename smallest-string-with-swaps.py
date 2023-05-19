class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #===>>> this is declaring parent as reperensenting them selves
        parent = defaultdict()
        for i in range(len(s)):
            parent[(s[i],i)] = (s[i],i)
        #====>>>> this is finding function with path comprenstion
        def find(x):
            if x ==  parent[x]:
                return x
            return find(parent[x])
        #==>>> here i'm joining pairs by least lexiographical element
        for pair in pairs:
            parent1 = find((s[pair[0]],pair[0]))
            parent2 = find((s[pair[1]],pair[1]))
            if parent1 < parent2: 
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2
        res = defaultdict(list)
        #===>>>> for collection of reperesentative
        for i in range(len(s)):
            res[find((s[i],i))].append((s[i]))
        #==>>> sort connected one 
        for i in res:
            res[i].sort(reverse=True)
        ans = []
        #====>>>> collect the answer
        for i in range(len(s)):
            ans.append(res[find((s[i],i))].pop())
    
        return "".join(ans)