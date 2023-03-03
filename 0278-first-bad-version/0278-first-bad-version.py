# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n
        ans = 0
        #===>>> for left less than right find the least bad version
        while left <= right :
            mid = (left+right)//2
            #==>>> if mid is bad version update it on ans and make it ur right
            if isBadVersion(mid):
                right = mid-1
                ans = mid
            #==>> if not move ur left forward to mid
            else:
                left = mid+1       
        return ans

                        
            