class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        maxx = 0
        left = 0
        for right in range(len(fruits)):
            window[fruits[right]] += 1
            n = len(window.values())
            #==>>> if window length is less than 2 then decrease by one
            while n>2:
                window[fruits[left]] -= 1
                #==>> if value at left is 0 remove it
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                    n -= 1
                left += 1
            #===>>> finally update the max
            maxx = max(maxx, right-left+1)
        return maxx