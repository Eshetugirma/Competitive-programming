class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        #==>>> this is the function which calculate average of every subtree
        def traverse(root,trav):
            if not root:
                return
            traverse(root.left,trav) 
            trav.append(root.val) 
            traverse(root.right,trav)  
            return sum(trav)//len(trav) 
        #==>>> this i to count number of subtree that have average equal to node value
        counts = 0 
        def count(root): 
            nonlocal counts 
            if not root:
                return 
            if root.val == traverse(root,[]) : 
                counts += 1
            count(root.left)
            count(root.right)
            return
        count(root)
        return counts