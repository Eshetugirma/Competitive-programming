class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sorted_array = []
        count = Counter(nums)
        heap = []
        for key,val in count.items():
            heappush(heap,(val,-key))
        while heap:
            v,k = heappop(heap)
            for i in range(v):
                sorted_array.append(-k)
        return sorted_array