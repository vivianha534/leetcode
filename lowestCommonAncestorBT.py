#https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
#https://www.youtube.com/watch?v=9wWHSq0YDl8

#We always start at the root b/c that's always going to be an ancestor
#The split where p and q are, then the node where that split occurs is the lowest common ancestor
#If we ever reach the node itself, that's the common lowest ancestor
#Time complexity and space is O(n)


###Recursion
 class Solution:
     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q:'TreeNode') -> 'TreeNode':
         
         #store answer as nothing
         self.ans=None

         #dfs
         def dfs(node):
            if not node:
                return False
            
            #want to traverse the tree to see if left/right is an ancestor of p or q
            left = dfs(node.left)
            right = dfs(node.right)
            #if this node itself is p or q
            cur = node==p or node==q
            #if one of three scenarios are true, that means its the LCA
            if (left and right) or (cur and right) or (cur and left):
                self.ans = node
                return
            #if any of these are true that means it's an ancestor
            return left or right or cur
        
        dfs(root)
        return self.ans
            