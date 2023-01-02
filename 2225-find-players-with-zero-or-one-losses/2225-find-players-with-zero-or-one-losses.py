class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        n = max(chain(*matches))+1
       
        players = [0] * n
        
        for w, l in matches:
            if players[w]>=0:
                players[w]=1      # (1)
            if players[l]<0:
                players[l]-=1      # (2)
            if players[l]>=0: 
                players[l]=-1     # (3)
                
        lostZero,lostOne = [],[]
        for i in range(n):
            if players[i] == 1:
                lostZero.append(i)
            elif players[i] == -1:
                lostOne.append(i)
   
        return [lostZero,lostOne]