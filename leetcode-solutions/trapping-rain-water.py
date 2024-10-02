class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        current_max = [[0,0] for i in range(n)]
        left_max,right_max = 0,0
        # pre computed left max and right max at each bar
        for i in range(n):

            left_max = max(left_max,height[i])
            right_max = max(right_max,height[n-i-1])

            current_max[i][0] = left_max
            current_max[n-i-1][1] = right_max

        stored_rain = 0 
        # using pre computed maxs calculate the container content at each bars
        for i in range(n):
            stored_rain += min(current_max[i][0],current_max[i][1]) - height[i]

        return stored_rain
        

