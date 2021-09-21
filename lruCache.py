#https://www.youtube.com/watch?v=7ABFKPK2hD4
#it has a capacity so it's fixed size
#want to get value based on a key, if key doesn't exist return -1
#want to be able to put in key,value pairs
    #if key already esists, update otherwise add to cache
    #if we exceed capacity evict the least recently used key
#We can use a hash map to instantly look up the value of every key
    #size of hashmap can't exceep capacity
    #key can be same value that we use for our nodes
    #value can be a pointer to the node itself
#when we call a get on a key, that becomes the most recently used
    #can keep track of most and least recent using left (least recent) and right (most recent) pointers
    #this means we're going to be using a doubly linked list
        #hashmap doesn't need to be updated because value is a pointer to node
#When capacity is met
    #update LRU pointer 
    #replace the key
    #update MRU pointer
#Each node will have a key, val, prev, and next
    #LRU and MRU are dummy nodes

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        #need to store capacity b/c we want to know if we ever go over the capacity
        self.cap = capacity
        #hash map
        self.cache={} #map key to node
        #dummy nodes for LRU and MRU
        #left =LRU right =MRU
        self.left, self.right = Node(0, 0), Node(0,0)
        #want LRU and MRU to be connected initially
        self.left.next, self.right.prev = self.right, self.left

    #remove node from list
    def remove(self, node):
        #node is going to be the middle node so we just need to rearrange
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    #insert at right
    def insert(self,node):
        #inserting node to the middle
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            #todo update most recent (helper functions)
            #want to update our currentnode to be most recent b/c we just got it
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            #each key is mapped to a node so we can just do .val
            return self.cache[key].val
        #doesn't exist
        return -1        

    def put(self, key: int, value: int) -> None:
        #key already exists, update val
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        #b/c we have a doubly linked list, we need to insert it
        self.insert(self.cache[key])

        #checks if the length of our cache exceeds the capacity
        #if it does we evict LRU
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)