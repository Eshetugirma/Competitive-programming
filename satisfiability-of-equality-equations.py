class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequals = set()
        parent,rank = defaultdict(),defaultdict()
        #===>>>> declaring default parents and rank to start 
        for i in range(97,123):
            parent[chr(i)] = chr(i)
            rank[chr(i)] = 0
        #===>>> this the find functions
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        #===>>> this is the union function which repersent one with other by use of ranking
        def union(x,y):
            parent1 = find(x)
            parent2 = find(y)
            if parent1 == parent2: return
            if rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
        #===>>> here i add unequals to set and call union for the equals one
        for i in equations:
            a,b,c,d = i[0],i[1],i[2],i[3]
            if b == "=":
                union(a,d)
            else:
                #===>>> here i return false if equal character are give equal
                if parent[a] == parent[d]: return False
                inequals.add((a,d))
        #==>>> search for unequals if there is equals
        for a,b in inequals:
            if find(a) == find(b):
                return False
        return True