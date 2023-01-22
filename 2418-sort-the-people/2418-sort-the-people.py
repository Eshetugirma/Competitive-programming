class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            temp = max(heights[i:])
            index = heights.index(temp)
            names[i],names[index] = names[index],names[i]
            heights[i],heights[index] = heights[index],heights[i]
        return names
        