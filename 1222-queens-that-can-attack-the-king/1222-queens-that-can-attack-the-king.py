class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans=[]
        for horizontal in [-1,0,1]:
            for vertical in [-1,0,1]:
                for distance in range(1,8):
                    x=king[0]+horizontal*distance
                    y=king[1]+vertical*distance
                    if [x,y] in queens:
                        ans.append([x,y])
                        break
        return ans