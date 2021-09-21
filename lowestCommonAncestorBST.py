#BST https://www.youtube.com/watch?v=gs2LMfuOR9k&t=187s
#BT https://www.youtube.com/watch?v=Z6d-UM7fDMM

#This is diff from a BT
#We always start at the root b/c that's always going to be an ancestor
#The split where p and q are, then the node where that split occurs is the lowest common ancestor
#If both p and q are greater, go to the right, if lower go left
    #The new lowest common ancestor will be the node right/left respectively
#If we ever reach the node itself, that's the common lowest ancestor
#Time complexity is O(logn) space is O(1) b/c we don't need data structures

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #start at root
        cur = root
        
        #continue till we find our result
        #p and q are guranteed to exist in the tree
        #cur will never be null, but this is just a way to have the code execute till we find the LCA
        while cur:
            #go down right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            #go down left subtree
            elif p.val < cur.val and q.val<cur.val:
                cur=cur.left
            #split occurs or we found the node itself
            else:
                return cur

        