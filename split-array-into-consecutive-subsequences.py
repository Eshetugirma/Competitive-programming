class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        dic = defaultdict(list)
        for num in nums:
            if dic[num-1]:
                heappush(dic[num],heappop(dic[num-1])+1)
            else:
                heappush(dic[num],1)
        for val in dic.values():
            if val and val[0] < 3:
                return False
        return True