class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxima = max(heights)
        count = [0]*(maxima+1)
        temp = heights[:]
        temp2 = names[:]
        #==> adding their heights to counter
        for i in heights:
            count[i] +=1
        target = 0
        for i in range(len(count)-1,-1,-1):
            if count[i]:
                names[target] = temp2[temp.index(i)]
                heights[target] = i
                target += 1
        return names
                
        