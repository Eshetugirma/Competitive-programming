class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        count = Counter(nums)
        mn = min(count.values())
        ans = float('inf')
        # if len(count) == 1: return 1
        for i in range(1,mn+1):
            temp = 0
            flag = True
            for f in count.values():
                a = f//(i+1)
                b = f%(i+1)
                if not b: 
                    temp += a
                elif i - b <= a:
                    temp += a+1
                else:
                    flag = False
                    break
                # print(f,temp)
            if flag:
                ans = min(ans,temp)
        return ans