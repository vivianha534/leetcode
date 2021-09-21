 #you will be provided with a hit at a particular timestamp
 #have to maintain a record of the hit
 #when asked for the number of hits in the prev 5 mins given a timestamp, have to give that number
 #need to implement hit
    #parameter is time stamp (int starting from 1)
 #getHit has the current time stamp
    #returns the number of hits in the past 5 minutes
#naive way:
    #have a list that stores all hits, and for each hit we have a timestamp
    #when we have a getHit we loop through that list
    #This wouldn't scale if there were lots of hits per second
#scaleable way
    #Create a list with 300 elements to store the time of that hit, and another 300 length list to store the count of that time
    #time could be more than 300 so we can do timestamp % 300 as index to set the value in our 2 lists
    #when we try to getHits we do currentTimeStamp - 300

class HitCounter:
    def __init__(self):
        #create 2 lists
        self.time = [0] * 300
        self.hits = [0] * 300
    
    def hit(self, timestamp: int) -> None:
        #everytime we get a hit we get the index first
        index = timestamp % 300

        #this means we're in a new 5 min cycle
        if self.time[index] !=timestamp:
            #update index with current timestamp
            self.time[index] = timestamp
            self.hits[index] = 1
        #we're in the same 5 min cycle so we just increase the hit
        else:
            self.hits[index] += 1
    
    def getHits(self,timestamp:int) -> int:
        result = 0

        #loop through to get hits
        for i in range(300):
            #within the past 5 mins
            if self.time[i] > timestamp - 300:
                result += self.count[i] 

        return result
