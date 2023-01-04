class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        minn=float('inf')
        index=-1
        for i , v in enumerate(points):
            if v[0]==x or v[1]==y:
                man_dis=abs(x - v[0]) + abs(y - v[1])
                if(man_dis<minn) :
                    minn=man_dis
                    index=i
        
        return index