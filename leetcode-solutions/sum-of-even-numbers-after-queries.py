class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        add = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                add+=nums[i]
        lst=[]
        for i in range(len(queries)):
            prev=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            curr=nums[queries[i][1]]
            if prev%2==0:
                if curr%2==0:
                    add+=(curr-prev)
                else:
                    add-=prev
            else:
                if curr%2==0:
                    add+=curr
            lst.append(add)
        return lst