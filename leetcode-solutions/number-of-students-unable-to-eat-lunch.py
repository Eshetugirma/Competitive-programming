class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        n, k = len(students), 0
        while k < n and count[sandwiches[k]]:
            count[sandwiches[k]] -= 1
            k += 1
        return n - k