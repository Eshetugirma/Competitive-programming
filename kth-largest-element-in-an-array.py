class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 
        pivot = random.choice(nums)
        left = []
        right = []
        mid = []
        #==>> always divide the element in nums to three parts
        for num in nums:
            if pivot < num:
                right.append(num)
            elif pivot > num:
                left.append(num)
            else:
                mid.append(num)
        #==>>> if len of right is greater than k then see answer in right else in left or mid
        if len(right) >= k:
            return self.findKthLargest(right,k)
        elif len(right) + len(mid) < k:
            return self.findKthLargest(left,k - len(right) - len(mid))
        else:
            return mid[0]