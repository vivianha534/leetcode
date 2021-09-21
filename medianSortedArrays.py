#given two arrays that are already sorted but could be diff sizes
#want to put them together and find the median
#want to do it in O(log(m+n))
#in most cases when we want log, we need to use binary search

#We're given 2 arrays, B and A
    #The left and right partition are the same size
    #We can simulate a combined array
        #We want our left partition to be roughly half (round down)
        #have a left and right pointer that points at array A
        #find the median of array A (using binary search) and include it in the left partition
        #for array B we can do half - # of elements from array A = # of elements in left partition from B
        #These 2 subarrays make up our left partition
            #To know if we foun the right partition, we check that the largest number of leftPartition A is smaller than the smallest number of rightPartition B and vice versa
    #If our left partition is not correct then we can move the left pointer to median+1, and recompute the middle of A
        # recalculate # elements from B by doing half - elements from A
        # check that the left partition is correct
#Odd
    #To find the median we take the min(smallest right partition A, smallest right partition B)
#Even
    #(Max(biggest number left partition A, biggest number left partition B ) + min(smallest number right partition A, smallest number right partition B)) / 2

#Edge case: Want all of left partition to be from one single array


#log(min(n, m)) <- running binary search on the smaller of the 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        #tells us total elements in left partition
        half = total // 2

        #only need to run BST on one of the arrays b/c half - left partition A ensures this
        #ensure that A is the samller of the 2
        if len(B) < len(A):
            A,B = B,A
        
        #run binary search on A b/c it's the smaller one
        l, r = 0, len(A) - 1

        #start looping and run binary search
        while True:
            #compute middle val of array A that we'll use to get left parition
            i = (l + r) // 2 #A
            #subtract by 2 b/c j is the index of the midpoint so we subtract 2 b/c arrays start at 0
            j = half - i - 2 #B

            #get the vals that we need to compare in order to make sure we have the correct left partition
            #any of these could be out of bounds so we account for it
            Aleft = A[i] if i >= 0 else float("-infinity")
            #if i + 1 is out of bounds that means we want all of A to be in partition
            Aright = A[i+1]  if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float ("infinity")

            #partition is correct
            if Aleft <= Bright and Bleft <= Aright:            
                #odd  total
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2
            #partition has too many elements from A
            elif Aleft > Bright:
                #reduce the size of left partition from A
                r = i-1
            #increase the size of left partition from A
            else:
                l = i + 1
