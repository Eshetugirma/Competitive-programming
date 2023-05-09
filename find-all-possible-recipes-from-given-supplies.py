class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        if not supplies: return []
        connect = defaultdict(list)
        indegre = defaultdict()
        ans = []
        
        for i in range(len(recipes)):
            indegre[i] = len(ingredients[i])
            for j in range(len(ingredients[i])):
                connect[ingredients[i][j]].append(i)

        que = deque(supplies)
        while que:
            curr = que.popleft()
            for index in connect[curr]:
                if index in indegre:
                    indegre[index] -= 1
                if indegre[index] == 0:
                    que.append(recipes[index])
                    ans.append(recipes[index])
                
        return ans