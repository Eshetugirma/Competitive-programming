class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        heap = []
        for i,j in dic.items():
            heappush(heap,(-j,i))
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        return ans

