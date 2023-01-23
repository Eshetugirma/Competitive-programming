class Solution:
    def minimumSum(self, num: int) -> int:
        new1 = []
        new2 = []
        num = sorted(list(str(num)),reverse=True)
        num = ''.join(num)
        num = list(num.rstrip('0'))
        if len(num) <= 1:
            return int(''.join(num))
        for i in range(len(num)):
            if i%2 == 0:
                new1.append(num.pop())
            else:
                new2.append(num.pop())
        minimum = int(''.join(new1)) + int(''.join(new2))
        return minimum