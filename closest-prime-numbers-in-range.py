class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        stack = []
        #==>>> first find all prime number between left and right 
        for curr in range(left,right+1):
            start = 2
            while start*start <= curr:
                while not curr%start :
                    if left <= start <= right and ( start > stack[-1] or not stack):
                        if stack and start - stack[-1] <= 2:
                            return [stack[-1],start]
                        stack.append(start)
                    curr //= start
                if start == 2:
                    start += 1
                else:
                    start += 2
            if curr != 1 and left <= curr <= right:
                if not stack or (curr > stack[-1]):
                    if stack and curr - stack[-1] <= 2:
                        return [stack[-1],curr]
                    stack.append(curr)
        dic = defaultdict(list)
        mn = right+1
        i = 0
        #==>> find minimam distance and return val at minimum distance 
        while i < len(stack)-1:
            mn = min(mn,stack[i+1]-stack[i])
            if (stack[i+1] - stack[i]) not in dic:
                dic[stack[i+1]-stack[i]] = [stack[i],stack[i+1]]
            i += 1
        return dic[mn] if dic else [-1,-1]