class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people)-1
        left = 0
        boats = 0
        while right >= left:
            if people[right]+people[left] <= limit:
                boats += 1
                right -= 1
                left += 1
            else:
                right -= 1
                boats += 1
        return boats
        