class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        mx = max(count.values())
        answer = [[] for i in range(mx)]
        # print(answer)
        for key,val in count.items():
            for i in range(val):
                # print(key,i)
                answer[i].append(key)
        return answer