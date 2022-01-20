'''
Level: Medium    Tag: [Stack]

Suppose we have a file system that stores both files and directories.

An example of one system is represented in the following picture:

"../../../Material/mdir.jpeg"

Here, we have dir as the only directory in the root.

dir contains two subdirectories, subdir1 and subdir2.

subdir1 contains a file file1.ext and subdirectory subsubdir1.

subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.

In text form, it looks like this (with ⟶ representing the tab character):

dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext
If we were to write this representation in code, it will look like this:

"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".

Note that the '\n' and '\t' are the new-line and tab characters.

Every file and directory has a unique absolute path in the file system,

which is the order of directories that must be opened to reach the file/directory itself,

all concatenated by '/'s. Using the above example,

the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext".

Each directory name consists of letters, digits, and/or spaces.

Each file name is of the form name.extension,

where name and extension consist of letters, digits, and/or spaces.

Given a string input representing the file system in the explained format,

return the length of the longest absolute path to a file in the abstracted file system.

If there is no file in the system, return 0.



Example 1:

"../../../Material/dir1.jpeg"

Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.

Example 2:

"../../../Material/dir2.jpeg"

Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longest absolute path to a file.

Example 3:

Input: input = "a"
Output: 0
Explanation: We do not have any files, just a single directory named "a".


Constraints:

1 <= input.length <= 104
input may contain lowercase or uppercase English letters, a new line character '\n', a tab character '\t', a dot '.', a space ' ', and digits.





=========== 2020 Description ============




Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.

subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.

subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.

For example, in the second example above,

the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",

and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,

return the length of the longest absolute path to file in the abstracted file system.

If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path,

if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.


'''


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        ans = 0
        totalLength = 0
        stack = [(-1, 0)]

        for p in input.split('\n'):
            currDepth = p.count('\t')
            currLength = len(p.replace('\t', ''))
            depth, length = stack[-1]
            while depth >= currDepth:
                totalLength -= length
                stack.pop()
                depth, length = stack[-1]

            if currDepth > 0:
                currLength += 1
            if p.count('.'):
                ans = max(ans, totalLength + currLength)
            totalLength += currLength
            stack.append((currDepth, currLength))

        return ans














    def lengthLongestPath2(self, input):
        """
        :type input: str
        :rtype: int
        """
        ans = 0

        paths = input.split("\n")
        stack = []
        for p in paths:


            if not stack:
                stack.append(p)
            elif p.count("\t") <= stack[-1].count("\t"):
                while stack and p.count("\t") <= stack[-1].count("\t"):
                    stack.pop()

                stack.append(p)

            else:
                stack.append(p)

            if p.count(".") > 0:
                full_path = ""
                for s in stack:
                    s = s.replace("\t", "") + "/"
                    full_path +=s
                ans = max(ans, len(full_path)-1 )

        print(ans)

        return ans





dir = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
assert 20 == Solution().lengthLongestPath2(dir)
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert 32 == Solution().lengthLongestPath2(input)

input = "a"
assert 0 == Solution().lengthLongestPath2(input)

input = "dir\n\t        file.txt\n\tfile2.txt"
assert 20 == Solution().lengthLongestPath2(input)

input = "a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"
assert 30 == Solution().lengthLongestPath2(input)

input = "file1.txt\nfile2.txt\nlongfile.txt"
assert 12 == Solution().lengthLongestPath2(input)


input = "dir\n        file.txt"
assert 16 == Solution().lengthLongestPath2(input)