class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict()
        #===>>> define the parent as default 
        for i in range(97,123):
            parent[chr(i)] = chr(i)
        #==>>> this is finding function which find the reperesentative of given character
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        #===>>> this to form connections we know from given two strings
        for i in range(len(s1)):
            x = find(s1[i])
            y = find(s2[i])
            if x == y:continue
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
        ans = []
        #===>>> here we find every minimum reperesentative of our target
        for el in baseStr:
            ans.append(find(el))
        
        return "".join(ans)