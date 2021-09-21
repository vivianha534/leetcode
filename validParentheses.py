 #Notice: We must start with an opening parentheses
    #After we start with an opneing parentheses, we can add as many opening parentheses as we want
        #as long as we eventually close it
#Once we add a closing parentheses that matches, we can remove that and its corresponding opener 
#if at the end we have an empty list than we can return true
#Notice: as we add closing parenthese, we remove from the beginning of the list
    #we're always removing from the top of the stack
#Use a hashmap to determine whether a closing parenthese matches an open parenthese
    #if we have a closing parethense we go up to hash, go back to stack, and check if they match
#Big O(n) time b/c we only go through the string once 
#O(n) space b/c we're using a stack and the stack will only be as big as the inputs

class Solution:
    def isValid(self, s:str) ->bool:
        stack = []
        #hashmap
        closeToOpen = {")" : "(", "]": "[", "}": "{"}

        #go through every character in input string to build stack
        for char in s:
            #this means it's a closing parenthese
            if char in closeToOpen:
                #make sure it's not an empty stack b/c if it is it's not valid
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                #closing parenthese does not match the opening parenthese
                else:
                    return False
            #if we get an open parenthese
            else:
                stack.append(c)
        #can only return true if the stack is empty
        return True if not stack else False