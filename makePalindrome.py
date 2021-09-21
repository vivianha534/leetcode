# 1. Count occurrences of all characters. 
# 2. Count odd occurrences. If this count is greater than 1 or is equal to 1 and length of the string is even then obviously palindrome cannot be formed from the given string. 
# 3. Initialize two empty strings firstHalf and secondHalf. 
# 4. Traverse the map. For every character with count as count, attach count/2 characters to end of firstHalf and beginning of secondHalf. 
# 5. Finally return the result by appending firstHalf and secondHalf

# Python3 program to rearrange a string to
# make palindrome.
from collections import defaultdict


def getPalindrome(st):

	# Store counts of characters
	hmap = defaultdict(int)
	for i in range(len(st)):
		hmap[st[i]] += 1

	# Find the number of odd elements.
	# Takes O(n)
	oddCount = 0

	for x in hmap:
		if (hmap[x] % 2 != 0):
			oddCount += 1
			oddChar = x

	# odd_cnt = 1 only if the length of
	# str is odd
	if (oddCount > 1 or oddCount == 1 and
			len(st) % 2 == 0):
		return "NO PALINDROME"

	# Generate first halh of palindrome
	firstHalf = ""
	secondHalf = ""

	for x in sorted(hmap.keys()):

		# Build a string of floor(count/2)
		# occurrences of current character
		s = (hmap[x] // 2) * x

		# Attach the built string to end of
		# and begin of second half
		firstHalf = firstHalf + s
		secondHalf = s + secondHalf

	# Insert odd character if there
	# is any
	if (oddCount == 1):
		return (firstHalf + oddChar + secondHalf)
	else:
		return (firstHalf + secondHalf)


s = "mdaam"
palindrome1=[]
palindrome1.append(getPalindrome(s))
print(getPalindrome(s))
print(palindrome1)

# This code is contributed by ukasp
