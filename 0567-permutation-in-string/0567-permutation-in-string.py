class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checker = False
        given = Counter(s1)
        window = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)):
            if given == window:
                checker = True
                break
            else:
                window[s2[i]] -= 1
                if window[s2[i]] == 0:
                    del window[s2[i]]
                window[s2[i+len(s1)]] += 1
        if window == given:
            return True
        return checker
            