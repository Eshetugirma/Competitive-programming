class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(pow(c,0.5))
        left = 0
        while right >= left:
            # print(right*right + left*left, left, right)
            if right*right + left*left == c:
                return True
            elif right*right + left*left > c:
                right-=1
            else:
                left += 1
        return False
        