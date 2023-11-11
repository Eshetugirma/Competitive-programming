class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = defaultdict(int)
        cows = defaultdict(int)
        a,b = 0,0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                bulls[secret[i]] += 1
                cows[guess[i]] += 1
        for el in bulls:
            b += min(bulls[el] , cows[el])
            # print(b)
        return str(a)+"A"+str(b)+"B"