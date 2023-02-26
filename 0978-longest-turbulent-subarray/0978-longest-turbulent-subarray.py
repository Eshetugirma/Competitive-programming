class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        maxx = 0
        ans = 1
        #===>>> find longest subarray for greater number at odd index
        for right in range(1,len(arr)):
            #==>> if val at even index is less update window unless update ur starting pointer
            if right%2 == 0:
                if arr[right] < arr[right-1]:
                    maxx = max(maxx,right-left+1)
                else:   
                    left = right  
            #==>> if val at odd index is greater update window unless update ur starting pointer
            else:
                if arr[right] > arr[right-1]:
                    maxx = max(maxx,right-left+1)
                else:
                    left = right
        ans = max(maxx,ans)
        left = 0
        maxx = 0
        #===>>> find longest subarray for greater number at even index
        for right in range(1,len(arr)):
            #==>> if val at odd index is less then update ur window unless update ur starting pointer
            if right%2 != 0:
                if arr[right] < arr[right-1]:
                    maxx = max(maxx,right-left+1)
                else:   
                    left = right 
            #==>>> if val at even index is greater update ur window 
            else:
                if arr[right] > arr[right-1]:
                    maxx = max(maxx,right-left+1)
                else:
                    left = right
        return max(ans,maxx)
        