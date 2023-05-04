class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        dic2 = defaultdict(list)
        heap = []
        #===>>>> heapify max heap by freq and lexicographically order
        for i,j in dic.items():
            heappush(heap,(-j,i))


        #==>>> collect k most frequent and return their list
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])

        return ans