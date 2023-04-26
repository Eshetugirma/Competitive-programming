"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {e.id:e for e in employees}
        def dfs(e) :
            imprtance = dic[e].importance
            for sub in dic[e].subordinates:
                imprtance += dfs(sub)
            return imprtance
        return dfs(id)