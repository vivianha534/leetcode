#We can iterate through the list and figure out where to place it
    #O(n*K) b/c there's k lists with at most n nodes
    #not efficient
#We can use the merge sort algorithim
    #divide and conquer algorithim
    #divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves
    #This is O(nlogk) - log k because we're dividng our lists in half when we sort them


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #return empty linked list
        if not lists or len(lists) == 0:
            return None

        #take pairs of linked lists and merge them each time until there's only one left
        while len(lists) > 1:
            mergedList = []
            
            #want to do pairs of linked lists, so incrementer is 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                #might be out of bounds if we have odd number of lists
                #it's ok to merge a list and a null list
                l2 = lists[i+1] if (i+1) < len(lists) else None

                #append to mergeLists variable where we store lists after we merge them
                mergedLists.append(self.mergeList(l1,l2))
            
            lists = mergedLists
        
        return lists[0]

    def mergeList(self, l1, l2):
        #create a dummy node so you can avoid the edge case of the initial empty list
        #this is the head of the list
        dummy = ListNode()
        tail = dummy
        
        #iterate while both lists are non empty
        while l1 and l2:
            #if list 1 is less than val of list2
            #take list1 and insert it to tail
            #update list 1 pointer
            if l1.val < l2.val:
                tail.next=l1
                l1=l1.next
            #list 2 is inserted
            #update list 2 pointer
            else:
                tail.next=l2
                l2=l2.next
            
            #update tail pointer
            tail=tail.next

        #if one of the lists is empty but the other isn't
        if l1:
            tail.next = l1
        elif l2: 
            tail.next = l2

        return dummy.next