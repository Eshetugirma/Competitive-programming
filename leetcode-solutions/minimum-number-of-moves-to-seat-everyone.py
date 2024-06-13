class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        movements = 0
        for i in range(len(seats)):
            movements += abs(seats[i]-students[i])

        return movements