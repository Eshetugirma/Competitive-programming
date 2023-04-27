class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append(0)
        while queue:
            pop = queue.popleft()
            for i in rooms[pop]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                if len(visited) == len(rooms):
                    return True
        return False