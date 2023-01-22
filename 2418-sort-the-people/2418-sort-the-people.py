class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # ==> solved with insertion sort
        for i in range(1,len(heights)):
            key_name = names[i]
            key_height = heights[i]
            right = i-1
            # ==> this loop is to shift sorted elememts up to see the suitable place for current value
            while right >= 0 and key_height > heights[right]:
                heights[right+1] = heights[right]
                names[right+1] = names[right]
                right -= 1
            # ==> put here in sorted part current value 
            heights[right+1] = key_height
            names[right+1] = key_name
        return names