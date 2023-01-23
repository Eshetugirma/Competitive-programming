class Solution:
    def minimumSum(self, num: int) -> int:
        new1 = []
        new2 = []
        # ==>> after int is changed to list then strip all right zeros of reverse sorted list
        num = sorted(list(str(num)),reverse=True)
        num = ''.join(num)
        num = list(num.rstrip('0'))
        # ==>> if length of num after striped is one then return int in num
        if len(num) == 1:
            return int(''.join(num))
        # ==>> this is to append minimum in to both new1 and new2
        for i in range(len(num)):
            if i%2 == 0:
                new1.append(num.pop())
            else:
                new2.append(num.pop())
        # ==>> return the min sum
        return int(''.join(new1)) + int(''.join(new2))