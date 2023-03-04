class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        stack = []
        #==>> find counter of smallest lexicogra character in wards 
        for word in words:
            
            word = sorted(word)
            count = Counter(word)
            stack.append(count[word[0]])
        #==>>> sort in decreasing order => count of words and check for queries how many in word is greater
        stack.sort(reverse=True)
        for i in range(len(queries)):
            
            query = sorted(queries[i])
            count = Counter(query)
            target = count[query[0]]
            
            left = 0
            right = len(stack)
            #==>>> use binary search to get the as fast as we can 
            while left < right:
                mid = (left+right)//2
                if stack[mid] <= target:
                    right = mid
                else:
                    left = mid+1
                    
            ans.append(right)
        return ans