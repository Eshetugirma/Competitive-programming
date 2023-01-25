class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        # ===>>>>> check if my pointers cover all elements in height
        while right > left:
            # ===>>>>> calculate the area at each point
            max_area = max(max_area,(right-left)*min(height[left],height[right]))
            # ==>> move the less pointing pointer 
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            max_area = max(max_area,(right-left)*min(height[left],height[right]))
        return max_area