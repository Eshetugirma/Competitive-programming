# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def count(root):
            if not root:
                return
            dic[root.val] += 1
            count(root.left)
            count(root.right)
        count(root)
        val = max(dic.values())
        mode = []
        for num in dic:
            if val == dic[num]:
                mode.append(num)
        return mode