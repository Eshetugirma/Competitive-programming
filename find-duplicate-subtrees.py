# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        holder = defaultdict(int)
        ans = []
        # temp = []
        def dfs(node):
            # nonlocal temp/
            if not node: return ''
            
            # print(node.val,temp)

            left = dfs(node.left)
            right = dfs(node.right)
            temp = f'l{left}{node.val}{right}r'
            holder[temp] += 1
            if holder[temp] == 2:
                ans.append(node)
            return temp
        dfs(root)
        # print(holder)
        
        # que = deque([root])
        # while que:
        #     node = que.popleft()
        #     key = dfs(node,[])
        #     holder[key] += 1
        #     ans[key] = node
        #     if node.left:
        #         que.append(node.left)
        #     if node.right:
        #         que.append(node.right)
        # res = []
        # for key,val in holder.items():
        #     if val > 1:
        #         res.append(ans[key])
        # print(holder)
        return ans