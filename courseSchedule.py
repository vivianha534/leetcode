#graph problem
#numCourses are the nodes
#prerequisites are edges
#we can use dfs to solve this
#we can use a datastructure called an adjacency list (will use a hashmap to rep this)
    #for each course will have a list of all its pre-reqs
#run dfs on every node from 0 to n-1
    #we have our prereq map so we'll do it recursively
    #if a course has no prereqs, then it can be completed
    #once a course is completed, and if its a prereq for another course, it can be removed
    #if a course's prereq(s) are completed, then the prereqs can be removed so it's an empty list so we know its completed
#O(n+p) n = number of courses p=#preReqs
#if there's a cycle then it's impossible
    #to know if there's a cycle we can use a set to keep track of what's been visited
    #will have list of courses that we're currently visiting along our dfs
        #if a course shows up twice within the set then there's a loop and we should return false

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create prereq map
        #for every course, initilly map it to an empty list
        preMap = {i:[] for i in range(numCourses)}

        #get each crs and prereq pair
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        #visitSet stores all courses along current DFS path
        visitSet = set()

        def dfs(course):
            #base case
            #if course is already in visit set aka there exists a loop
            if course in visitSet:
                return False
            #prereq list is empty aka the course can be completed
            if preMap[course] == []:
                return True
            
            #currently visiting this course
            visitSet.add(course)

            #recursiviely run dfs on its pres
            for pre in preMap[course]:
                #if we find one course that can't be completed, then it returns false
                if not dfs(pre): return False

            #no longer visitng, finished visiting
            visitSet.remove(course)
            #b/c we know this course can be visited we can set it to an empty list so if we ever need to do dfs again we'll just return true immediately
            preMap[course] = []
            #if previous if statement doesn't run than that means this is a course that can be taken and we want to return true
            return True
        
        #need to call dfs for every course
        #we need to iterate this way b/c there's no gurantee that all courses are connected, there could be seperate graphs
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
