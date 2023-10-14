class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = {('N','L'):'W',('N','R'):'E',('S','L'):'E',('S','R'):'W',('W','L'):'S',('W','R'):'N',('E','L'):'N',('E','R'):'S',('W','R'):'N'}
        p = {'N':(0,1),'E':(1,0),'W':(-1,0),'S':(0,-1)}
        # print(directions)
        n = len(instructions)
        curr = 'N'
        seen = set((0,0))
        position = [0,0]
        for i in range(n):
            inst = instructions[i]
            if inst == 'L' or inst == 'R':
                curr = directions[(curr,inst)]
            else:
                position[0],position[1] = position[0]+p[curr][0],position[1]+p[curr][1]
                # if tuple(position) in seen and i == n-1: return True
                # seen.add(tuple(position))
            print(position,curr)
        return curr != 'N' or tuple(position) == (0,0)