class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        running_product = 1
        ans1 = [1]
        ans2 = [1]
        #==>>> collect forward prefix prodact into ans1
        for i in range(n):
            running_product *= nums[i]
            ans1.append(running_product)
        nums.reverse()
        running_product = 1
        #==>>> collect backward prefix product into ans2
        for i in range(n):
            running_product *= nums[i]
            ans2.append(running_product)  
        #==>>> update product of arr into nums without self multply
        for i in range(1,n+1):
            nums[i-1] = ans1[i-1]*ans2[n-i]
        return nums