##To be valid:
#root value can be any value
    # -infinity < root < infinity
# the left subtree should be such that -infinity < cur < root
#right subtree root < cur < infinity
    #right subtree prev < cur < infinity
    #left subtree  -infinity < cur < prev


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #best way to implement is recursively
        def valid(node, left, right):
            #empty tree is still valid
            if not node:
                return True
            
            #found a node that broke valid tree
            if not (node.val < right and node.val > left):
                return False
            
            #want to make sure left subtree is valid
            #since we're going left, then we can leave left the same, but we need
            #it to be less than the parent
            return (valid(node.left, left, node.val) and

            #want to make sure right subtree is valid
            #right boundary stays same, left boundary is updated
            valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))