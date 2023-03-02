class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        #==>> sort speed by thier position 
        position, speed = zip(*sorted(zip(position, speed)))
        for i in range(len(speed)):
            #==>> calculate total time needed from every position 
            time.append((target-position[i])/speed[i])
        stack = [time[0]]
        i = 1
        #==>> form monotonically increasing order of time needed
        while i < len(time):
            if stack and stack[-1] <= time[i]:
                stack.pop()
            else:
                stack.append(time[i])
                i += 1  
        return len(stack)