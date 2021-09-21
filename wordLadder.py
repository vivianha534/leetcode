#https://www.youtube.com/watch?v=h9iTnkgv05E
#want to create a sequence from beginWord to endWord
#beginWord doesn't need to be in wordList but every other word in the sequence does
#every adjacent pair of words differs by a single character
#every single word is going to be guranteed to be the exact same length
#this looks like a graph problem
    #want to go from beginning word to end word
    #go from one word to another word to another word
    #will have bidirectional edges
#first build an adjacency graph
    #we know for any word we want at most 1 character diff
    #we can take a word and see what it will look like if we change one character
        #ex) hot -> *ot
        #       -> h*t
        #       -> ho*
        #ex) dot -> *ot
        #       -> d*t
        #       -> do*
        #we can create a hashmap where the key is the pattern, and the value is everyword that fits that pattern
        #ex) {*ot : [hot, dot, lot]}
        #to find all the neighbors of hot, we find all of the patterns, and use the pattern to traverse the hash map
    #O(n*m^2) n from going through every word in list, m from every character we remove from word, another m to add each word to list
#after getting adjacency graph we can do a bfs to get shortest path

class Solution:
    def ladderLength(self,beginWord: str, endWord: str, wordList: List[str]) -> int:
        #check to see that endWord is in wordList, if not return 0
        if endWord not in wordList:
            return 0
        
        #dictionary where if you insert a new value for the first time, the default value is an empty list
        neighbors = collections.defaultdict(list)
        #append beginWord cause it's not part of wordList initially
        wordList.append(beginWord)

        #start to build adjacency list
        for word in wordList:
            #find every possible pattern for each word
            for j in range(len(word)):
                #take jth character and replace it with * and get the remaining chars, skipping the jth one
                pattern = word[:j] + "*" + word[j+1:]
                #for this pattern we're gonna add the word to the neighbors dictionary
                #will help us traverse the graph later on
                neighbors[pattern].append(word)
    
        #bfs
        #don't want to visit the same word twice
        visit = set([beginWord])
        #continue popping until we get to the end word
        q=deque([beginWord])
        #have at least 1 word initially
        result=1

        #while queue is non empty
        #if we find word we return result, if we don't when the loop exists we return 0
        while q:
            #go through entire layer and keep going layer by layer until queue is empty
            for i in range(len(q)):
                #go through every single node and pop that node
                word = q.popleft()
                if word ==endWord:
                    return result
                #take neighbors of word and add to queue
                #first need to get the every pattern of the word and look into neighbors to see what's it's neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbors[pattern]:
                        #won't get same word b/c we'll check that it's not visited
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res+=1
        return 0
