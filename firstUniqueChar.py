#find first non-repeating character and return its index
    #if it does not exist return -1
#One way: Using nested loops
    #Not the best b/c O(n^2)
#Second way: Counting the number of times a letter occurs and then iterating through the string
    #Datastructure that can hold a key:value -> letter: # of occurences -> dictionary
    #for loop iterating through string to find first character that only has one occurence

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterOccurences = collections.Counter(s) #letter: # of occurences
        
        for idx, ch in enumerate(s):
            if letterOccurences[ch] == 1:
                return idx
        
        return -1