#ALGO EXPERT
#every node to the left has to be strictly less than
#every node to the right has to be greater than or equal to
#insertion
    #call insertion on bst and start comparing the nodes
    #we can eliminate subtrees as we notice that the number is greater than or less than
#searching
    #we call searching on the bst
    #compare nodes
    #can eliminate subtrees
    #very similar to insertion
#deletion
    #call search if you don't find it, don't need to do anything
    #if you do find it
        #if it has no children we can just erase it and replace it with null
    #if it has one child
        #remove parent, and connect the child to the grandparent
    #if it has two full children
        #grab the smallest value in the right subtree of that node (left most value in the right subtree) replace the value we're deleting with this
            #this works b/c since this was in the right subtree, it will be greater than all of left subtree
            #b/c it was the left most in the right subtree, then it's smaller than everything else in the right subtree
        #delete the smallest value in right subtree
#Time Complexity
    #O(log(N)) - N is number of nodes
        #We didn't go through the entire tree, we eliminated half of the tree each time we used our functions
    #worst case O(N)
        #Only left or right nodes, so we have to go through the entire tree
#Space
    #if you do it recursively (b/c it takes up space on the call stack)
        #Avg = O(log(N))
        #Worst = O(N) 
    #If you do it iteratively
        #Avg = worst = O(1) (b/c not storing in stack)

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        #left and right nodes
        self.left = None
        self.right = None

    def insert(self, value):
        #keep track of the current node we're at b/c when we call insertion, we call it on root, but when we traverse the tree we want to keep track of where we're at
        #= self b/c at the beginning, the current node, is the node we call insertion on, and that's self
        currentNode = self

        while True:
            #if value we want to insert is less than current value we want to go left
            if value < currentNode.value:
                #we're at the end of the branch
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                #still have left subtree
                else:
                    currentNode = currentNode.left
            #right subtree
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        #return so we can call insert function one after the other in test cases
            #testBst.insert(1).insert(5)
            #not really relevant to algorithim
        return self

    #searching algorithim
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            #go to left subtree
            if value < currentNode.value:
                currentNode = currentNode.left
            #go to right subtree
            elif value > currentNode.value:
                currentNode = currentNode.right
            #found the value
            else:
                return True
        #node is not found
        return False

    #parentNode is optional default none b/c root has no parent
    #approach: find node first, then remove
    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            #the value of the node we're trying to remove is less than current node
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            #found the node we're trying to remove
            else:
                #node we're removing has 2 children nodes
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    #currentNode.value = smallest value of right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                #don't have 2 children nodes
                    #2 cases: node has a parent, node does not have a parent (root)
                #root node doesn't have a parent node
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        #assign currentNode.left last b/c we need it to set the above lines
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        #assign currentNode.right last b/c we need it to set the above lines
                        currentNode.right = currentNode.right.right
                    #root doesn't have any children, so we're just deleting the BST
                    else:
                        currentNode.value = None
                        #if don't want to delete tree do pass
                #our current node is a left child
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                #our current node is a right child
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                #found the node so break out of the loop
                break
        return self
    
    #call this on right subtree to get min value of right tree to replace removed node w/ 2 children
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


