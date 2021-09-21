 #We could do O(n^2) approach using nested loops but this isn't ideal
 #We could use a stack (LIFO)
    #want to use a stack because then we can remember what the previous temp was and also keep track of the index
    #if we find a higher temp, we can pop the prev temp off the stack, and store a value in our output array
        #push the current temperature that we're looking at onto the stack
    #if we find a lower temp, then we can't pop from our stack, instead we add the lower temp to the stack
    #Notie: This is a monotonic decreasing stack
    #if we have an empty stack, just add the value to the stack
    #The output for the unpopped values is 0

#O(n) time and space

class Solution:
    def dailyTemperatures(self, temperatures: List[int]->List[int]):
        results=[0] * len(temperatures)
        stack = [] #pair: [temp,index]

        for idx, temp in enumerate(temperatures):
            #is our stack not empty, and if it is, is this temp greater than the top of the stack?
            #top of stack is stack[-1]
            while stack and temp>stack[-1][0]:
                stackT, stackIdx = stack.pop()
                results[stackIdx] = idx-stackIdx

            #append to the stack, the value we're currently traversing            
            stack.append([temp, idx])
        return res
