class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)-1):
            index = i
            for j in range(i+1,len(names)):
                if heights[index] < heights[j]:
                    index = j
            names[i],names[index] = names[index],names[i]
            heights[i],heights[index] = heights[index],heights[i]
        return names
        