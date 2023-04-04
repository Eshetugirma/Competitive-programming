class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        check = list(set(deck))
        target = dic[check[0]]
        #===>>> to be true all element must have equal count 
        stack = []
        for num in check:
            #==>>> if single element we can't partition
            if dic[num] <= 1:
                return False 
            stack.append(dic[num])
        gcd = math.gcd(*stack)
        if gcd > 1:
            mn = gcd
        else:
            mn = min(stack)
        for num in stack:
            if num%mn:
                return False
        return True