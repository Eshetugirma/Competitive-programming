class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                # print(i,j)
                if not (hours[i]+hours[j])%24:
                    count += 1
                    # break
        return count