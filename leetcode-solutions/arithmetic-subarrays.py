class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            new_nums = nums[l[i]:r[i]+1]
            new_nums.sort()
            left = 0
            right= 1      
            
            if len(new_nums) == 1:
                output.append(True)
                continue
            diff = new_nums[1] - new_nums[0]
                
            flag = True
            while right < len(new_nums):
                if new_nums[right] - new_nums[left] != diff:
                    flag = False
                    break
                
                left += 1
                right += 1
            output.append(flag)  
        return output