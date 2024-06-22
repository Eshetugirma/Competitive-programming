class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = []
        prefix = 0
        count = 0
        index = 0
        offset = -1
        #==>>>
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                arr.append(i)

        for i in range(len(nums)):
                prefix += nums[i]
                if prefix == k:
                    if offset < 0:
                        offset = arr[0]
                    count += offset+1
                elif prefix > k:
                    prefix -= 1
                    offset = arr[index+1]-arr[index] -1
                    count += offset+1
                    index += 1
        return count
