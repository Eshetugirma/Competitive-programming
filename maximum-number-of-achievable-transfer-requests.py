class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # net = [0]*n
        # impossible = 0
        for i in range(len(requests),0,-1):
            for combo in itertools.combinations(range(len(requests)),i):
                net = [0]*n
                for j in combo:
                    net[requests[j][0]] -= 1
                    net[requests[j][1]] += 1
                if not any(net):
                    return i
        return 0