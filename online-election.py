class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        vote = defaultdict(int)
        leading = []

        for i in persons:
            vote[i] += 1
            if vote[i] >= max(vote.values()):
                leading.append(i)
            else:
                leading.append(leading[-1])
        self.leading = leading
        
    def q(self, t: int) -> int:
        index = bisect_left(self.times,t)

        if index < len(self.times) and t == self.times[index] :
            i = index
        else:
            i = index - 1
        return self.leading[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)