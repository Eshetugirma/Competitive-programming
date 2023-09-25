class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inheritance = defaultdict(list)
        self.removed = set()
        self.k = kingName
        

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.removed.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        answer = []
        count = 0
        def dfs(parent):
            if not self.inheritance[parent]:
                return 
            for child in self.inheritance[parent]:
                ans.append(child)
                dfs(child)
        ans.append(self.k)
        dfs(self.k)
        for i in range(len(ans)):
            if ans[i] not in self.removed:
                answer.append(ans[i])
        return answer



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()