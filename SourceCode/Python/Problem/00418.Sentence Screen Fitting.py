'''
Level: Medium  Tag: [DP]

Given a rows x cols screen and a sentence represented by a list of non-empty words,

find how many times the given sentence can be fitted on the screen.


A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.

Example 1:
	Input: rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
	Output: 1

	Explanation:
	I-had
	apple
	pie-I
	had--

	The character '-' signifies an empty space on the screen.

Example 2:
	Input:  rows = 2, cols = 8, sentence = ["hello", "world"]
	Output:  1

	Explanation:

	hello---
	world---

	The character '-' signifies an empty space on the screen.

Example 3:
	Input: rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
	Output:  2

	Explanation:
	a-bcd-
	e-a---
	bcd-e-

	The character '-' signifies an empty space on the screen.


'''

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        rx = 0
        i = 0
        ans = 0
        while rx < rows:
            cx = 0
            while cx < cols:
                if cx + len(sentence[i]) <= cols:
                    cx += len(sentence[i]) + 1 # space = 1
                    i += 1
                else:
                    # 裝不下了，結束迴圈跳下一個row
                    break

                if i == len(sentence):
                    ans += 1
                    i = 0

            rx += 1

        print(ans)

        return ans








    def wordsTyping2(self, sentence, rows, cols):
		rx = 0
		cx = 0
		ans = 0
		n = len(sentence)
		i = 0
		while rx < rows:
			cx = 0
			while cx < cols:
				if len(sentence[i]) <= cols - cx:
					cx +=  len(sentence[i])+1
					if i < n-1:
						i += 1
					else:
						i = 0
						ans += 1
					if cx >= cols:
						break
				else:
					break
			rx += 1

		print(ans)
		return ans











rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]
assert 1 == Solution().wordsTyping2(sentence, rows, cols)


rows = 3
cols = 6
sentence = ["a", "bcd", "e"]
assert 2 == Solution().wordsTyping2(sentence, rows, cols)

rows = 2
cols = 8
sentence = ["hello", "world"]
assert 1 == Solution().wordsTyping(sentence, rows, cols)