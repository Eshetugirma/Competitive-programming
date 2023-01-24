class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers)-1
        # ==>> iterate until our left and right pointers are collide 
        while left < right:
            sums = numbers[left] + numbers[right]
            # ==>>> for sum less than our target then move right
            if sums > target:
                right -=1
            # ==>>> for sum greater than our target move left 
            elif sums < target:
                left +=1
            # ==>>> return one indexed indices of sum equal with target
            else:
                return [left+1,right+1]
        