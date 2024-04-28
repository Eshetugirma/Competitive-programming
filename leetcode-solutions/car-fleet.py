class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        #==>> sort speed by thier position 
        position, speed = zip(*sorted(zip(position, speed)))
        for i in range(len(speed)):
            #==>> calculate total time needed from every position 
            time.append((target-position[i])/speed[i])
            #==>> form monotonically increasing order of by time needed
            while len(time) >=2 and time[-1] >= time[-2]:
                time[-2] = time[-1]
                time.pop()
        return len(time)