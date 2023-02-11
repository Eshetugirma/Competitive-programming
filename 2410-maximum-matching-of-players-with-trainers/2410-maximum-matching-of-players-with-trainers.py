class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n = len(players)
        m = len(trainers)
        print(n,m)
        pointer1 = 0
        pointer2 = 0
        if n>m:
            k = m
        else:
            k = n
            pointer2 = m-n
        mymax = 0
        # ==>>> check if there is that type of maching in the lists
        for i in range(k):
            if trainers[pointer2] >= players[pointer1]:
                mymax += 1
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
        return mymax
            
                