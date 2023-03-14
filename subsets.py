class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        #==>>>> this is with out duplicate 
        def subset(index,temp):
            if index >= len(nums):
                return
             #===>>> always append to temp and copy to ans   
            temp.append(nums[index])
            ans.append(temp[::])
            #==>>> recursivly calling function 
            subset(index+1,temp)
            temp.pop()
            subset(index+1,temp)

        subset(0,[])
        return ans