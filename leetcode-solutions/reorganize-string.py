class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        
        for key,val in count.items():
            heappush(heap,[-val,key])
        stack = []
        while len(heap) > 1:
            a,b = heappop(heap),heappop(heap)
            if stack and stack[-1] == a[1]:
                stack.append(b[1])
                stack.append(a[1])
            else:
                stack.append(a[1])
                stack.append(b[1])
            a[0] += 1
            b[0] += 1
            if a[0] < 0:
                heappush(heap,a)
            if b[0] < 0:
                heappush(heap,b)
        # print(heap)
        if heap and heap[0][0] == -1:
            stack.append(heap[0][1])
        elif heap and heap[0][0] < -1:
            return ''
        return ''.join(stack)
