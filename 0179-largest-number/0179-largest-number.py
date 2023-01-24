class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # for each elements in nums check which is greater 
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                # ==>> change elements to string and add each enterchangebly for all case 
                sum1 = int(str(nums[i])+str(nums[j]))
                sum2 =int(str(nums[j])+str(nums[i]))  
                #==>>> then if the order them by the greater string sum 
                if sum1 <= sum2 :
                    nums[i],nums[j] = nums[j],nums[i]
        # ==>>> then change integer in list to string then join togethor
        
        ans = ''.join(list(map(str,nums)))
        # ==>> if our input is all zeros like [0,0,0,0,0,0,0,0] then we return one zero "0"
        return "0" if ans.lstrip("0")=="" else ans
        