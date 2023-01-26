class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        right = 0
        left = 0 
        # ==>>>> hold all elements in by updating their last occurance in dict last_index
        for i, c in enumerate(s):
            last_index[c] = i
        ans = []
        temp = 0
        # ==>>> iterate s to get see where is the minimum partition points
        for i,c in enumerate(s):
            left +=1 
            # ==>>> update last occurance of element in every partition
            right = max(right,last_index[c])
            # ==>> when my left pointer check that all element before right pointer they parted together 
            if left>right:
                ans.append(left-temp)
                temp = left
        return ans