class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dic[i+j].append(mat[i][j])
        ans = []
        for entry in dic.items():
            if entry[0] % 2 == 0:
                ans.extend(entry[1][::-1])
            else:
                ans.extend(entry[1])
        return ans