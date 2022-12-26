class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum = 0
        for i in range(len(salary)):
            sum += salary[i]
        sum = sum - salary[0] - salary[-1]
        return sum/(len(salary)-2)
    