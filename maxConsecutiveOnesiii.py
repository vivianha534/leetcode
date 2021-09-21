#https://www.youtube.com/watch?v=FQH1xNZz0tg
#goal: get the length of the longest contiguous consecutive ones
#can do up to K flips of 0s to 1s
#sliding window technique
    #used whenever the q asks for max, min, sum, or some other contstraint on a contiguous subarray
    #has 2 variants -> fixed size window, and variable size window
#Variable size - Can construct a window that accumulates as many ones as possible (have a start and end pointer)
    #construct a window that uses K flips to get the max 1s we can starting from the beginning
    #count the number of 1s that we have after K flips
    #as soon as the number of 0s exceeds k we contract the window
        #move the start over to the right until number of 0s < k
        #once the condition is valid, we can advance the end pointer
    #keep track of the number of 1s again

#while condition is valid -> advance e
#while condition is not valid advance s until it becomes valid

class Solution:
    def longestOnes(self, A:List[int], k:int) -> int:
        #keep track of number of zeroes, maxOnes, start
        zeroes, maxOnes, start = 0, 0, 0
        #when the end pointer reaches the end of the array, then we're done
        for end in range(len(A)):
            #if the end is pointing at a zero then increase the number of zeroes
            if A[end] == 0:
                zeroes +=1
            #check if we have more than k zeroes, if we do than we should advance start
            while zeroes > k:
                #if start was previously at 0 then advance start and decrease number of 0s
                if A[start] == 0:
                    zeroes -= 1
                #advance start
                start += 1
            #size of the current window b/c we already know we've kept our conditions valid
            #max b/c previous window may have had more ones
            maxOnes = max(maxOnes, end - start + 1)
            #increase end value
            end +=1
        return maxOnes