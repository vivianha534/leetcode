#https://shareablecode.com/snippets/max-consecutive-ones-ii-python-solution-leetcode-D6Wu-AMV9
#todo

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #prev is how many contiguous ones there were before our current value
    #curr represents the amount of contiguous ones we currently have
    result, prev, curr = 0, 0, 0
    for n in nums:
        if n == 0:
            #either we had a longer string of ones, or the zero we just flipped has more ones
            result = max(result, prev+curr+1)
            prev, curr = curr, 0
        else:
            curr += 1
    #take the min of the two b/c if the entire list is all 1's already then prev+curr+1 will be out of bounds
    return min(max(result, prev+curr+1), len(nums))

print(findMaxConsecutiveOnes([0,1,1]))