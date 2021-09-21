#DFS 
#for every node, we 're going to add it to the array, and for every child of that node we run dfs
#Time = O(v+e) - v is nodes, e is edges connecting nodes
    #we traverse every vertex O(v)
    #for every vertex, we iterate through the children and call dfs, and the size of that for loop will be the number of children (aka edges coming out of og node)
#Space = O(v) - our output array holds v different nodes
    #in the worst case scenario, we are adding a bunch of frames to the call stack (at worst v calls)

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

#input is a graph
#output is dfs results
class Node:
    def __init__(self, name):
        self.children = []
        #every node has a name
        self.name = name

    #can add a child to a node
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        #append the node to the array b/c we're calling dfs on the node
        array.append(self.name)
        for child in self.children:
            #for every child in children, we call dfs on the child
            child.depthFirstSearch(array)
        return array

