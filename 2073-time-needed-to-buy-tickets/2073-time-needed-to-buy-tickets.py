class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        #==>>> itarate and check if every port has less tickets than chosen 
        for i in range(len(tickets)):
            #==>> if greater add time needed for chosen else add individual time needed 
            if tickets[i] >= tickets[k]:
                if i <= k:
                    ans += tickets[k]
                else:
                    ans += tickets[k]-1
            else:
                ans += tickets[i]
        return ans