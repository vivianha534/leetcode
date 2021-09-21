#https://www.youtube.com/watch?v=A8NUOmlwOlM
#want to insert a new interval into the list of intervals
    #may need to merge b/c we don't want them to overlap
        #take min and max of overlap and make that the new interval
#cases:
    #no overlap
    #overlaps with one
    #overlaps w/ multiple
#To determine where new interval should go, we need to iterate over old intervals and find insertion point for new interval
#no overlap
    #find where the the interval would go and insert it accordingly and insert the existing ones according
#multiple overlap
    #we can see that there's overlap if the end val of A is not less than start val of B and start val of A is not greater than end val of B
        #new interval does not go before/after old interval
        #to merge we take min of two intervals, and max of two intervals
        #once we've merged the interval, we have to check if it overlaps with any other interval before we can put it in the output
#time and space complexity O(n) b/c need to iterate through list of intervals once b/c it's arlready sorted

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        #iterate through every single interval
        for i in range(len(intervals)):
            #edge cases
            #if newInterval goes before the current interval
            #newIntervalEnd < curIntervalStart
            if newInterval[1] < intervals[i][0]:
                #insert new interval
                result.append(newInterval)
                #we already know all of the intervals after won't overlap so we can just append
                return result + intervals[i:]
            #new interval goes after current interval
            #newIntervalStart > curIntervalEnd
            #We don't know if our newInterval will overlap with the other intervals yet so we don't want to append newInterval to results
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            #newInterval overlaps with current interval
            else:
                #merges intervals
                newInterval=[min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                #can't append newInterval yet b/c it could still merge with upcoming intervals
        
        #eventually add newInterval
        result.append(newInterval)

        return result