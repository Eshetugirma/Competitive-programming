class Solution:
    def getRow(self, rowIndex: int,arr=[1,1]) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex-1)
        curr = [1]
        for i in range(len(prevRow)-1):
            curr.append(prevRow[i] + prevRow[i+1])
        curr.append(1)
        return curr
