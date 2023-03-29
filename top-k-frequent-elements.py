class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums) 
        sorted_dic = sorted(dic,key= lambda x: dic[x])
        start = len(sorted_dic)-k
        return sorted_dic[start:]