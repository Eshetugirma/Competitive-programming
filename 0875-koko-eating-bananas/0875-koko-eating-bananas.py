class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        
        if len(piles) == 1:
            return piles[0]//h + int(piles[0]%h > 0)
        
        #==>>> use binary search on max and min of given piles
        while left <= right:
            mid = (left+right)//2            
            time = 0
            
            #==>>> find time needed to finish if k == mid
            for i in range(len(piles)):
                time += piles[i]//mid + int(piles[i]%mid > 0 )
                if time > h:
                    break
            
            #==>> if she finished in given time then take mid and update right
            if time == h :
                ans = min(mid,ans)
                right = mid-1
            
            #==>> also if she finished before given time update right to mid
            elif time < h:
                ans = min(mid,ans)
                right = mid-1
            
            #==>> if time needed is greater than time given move left
            else:
                left = mid+1
        
        return ans
                
            