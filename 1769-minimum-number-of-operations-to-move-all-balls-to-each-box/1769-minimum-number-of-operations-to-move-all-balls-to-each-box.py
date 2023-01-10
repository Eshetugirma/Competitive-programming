class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        ans = []
        left = 0
        right = sum(i for i in range(l) if boxes[i]=='1')
        one_left, one_right = 0, boxes.count('1')
        for i in range(l):
            ans.append(left+right)
            if boxes[i]=='1':
                one_left, one_right = one_left+1, one_right-1
            left, right = left+one_left, right-one_right
        return ans
