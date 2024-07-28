class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        nums = []
        for k,v in count.items():
            nums.append(v)
        nums.sort(reverse = True)

        summ = 0
        mn = 0
        n = len(arr)//2 + len(arr)%2
        # print(nums)
        for num in nums:
            summ += num
            mn += 1
            if summ >= n:
                return mn

        return mn