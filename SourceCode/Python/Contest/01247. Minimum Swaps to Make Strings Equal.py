'''

5247->1247. Minimum Swaps to Make Strings Equal
Difficulty: Easy
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.

Your task is to make these two strings equal to each other.

You can swap any two characters that belong to different strings, which means:

swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal,
or return -1 if it is impossible to do so.



Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation:
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2:

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation:
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4


Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.


'''

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if list(s1).sort() == list(s2).sort():
            return 0

        ans = 0
        s1 = list(s1)
        s2 = list(s2)


        for i in range(len(s1)):
            j = i
            while s1[j] != s2[i]:
                j += 1
            while i < j:
                s1[j] ,s1[j - 1] = s1[j - 1], s1[j]
                j -= 1
                ans += 1

        return ans







# Python3 implementation of the above approach

# Function that returns true if s1
# and s2 are anagrams of each other
def isAnagram(s1, s2) :
	s1 = list(s1)
	s2 = list(s2)
	s1 = s1.sort()
	s2 = s2.sort()

	if (s1 == s2) :
		return 1

	return 0

# Function to return the minimum swaps required
def CountSteps(s1, s2, size) :
	s1 = list(s1)
	s2 = list(s2)

	i = 0
	j = 0
	result = 0

	# Iterate over the first string and convert
	# every element equal to the second string
	while (i < size) :
		j = i

		# Find index element of first string which
		# is equal to the ith element of second string
		while (s1[j] != s2[i]) :
			j += 1

		# Swap adjacent elements in first string so
		# that element at ith position becomes equal
		while (i < j) :

			# Swap elements using temporary variable
			temp = s1[j]
			s1[j] = s1[j - 1]
			s1[j - 1] = temp
			j -= 1
			result += 1

		i += 1

	return result

# Driver code
if __name__ == "__main__":

	s1 = "xx"
	s2 = "yy"

	size = len(s2)

	# If both the strings are anagrams
	# of each other then only they
	# can be made equal
	if (isAnagram(s1, s2)) :
		print(CountSteps(s1, s2, size))
	else :
		print(-1)

# This code is contributed by AnkitRai01




