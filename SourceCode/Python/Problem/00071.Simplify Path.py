'''
Level: Medium  Tag: [Stack]

Given a string path,

which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,

convert it to the simplified canonical path.

In a Unix-style file system,

a period '.' refers to the current directory, a double period '..' refers to the directory up a level,

and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.

For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory
(i.e., no period '.' or double period '..')
Return the simplified canonical path.



Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op,
as the root level is the highest level you can go.

Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.


Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.


'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.replace("//", "/")
        path = path.rstrip("//")
        pname = path.split("/")
        stack = []
        for p in pname:
            if p == ".." and len(stack) > 0:
                stack.pop()
                continue
            if p != ".." and p != ".":
                stack.append(p)
        if len(stack) == 1:
            conon_path = "/" + stack[0]
        else:
            conon_path = "/".join(stack)


        conon_path = conon_path.replace("//", "/")
        conon_path = conon_path.rstrip("//")
        if len(conon_path) == 0:
            conon_path = "/"
        print(conon_path)

        return conon_path


path = "/home//foo/"
Solution().simplifyPath(path)

path = "/../"
Solution().simplifyPath(path)


path = "/b/c/a/../d/e"
Solution().simplifyPath(path)

path = "/a/./b/../../c/"
assert "/c" == Solution().simplifyPath(path)

path ="/a/../../b/../c//.//"
assert "/c" == Solution().simplifyPath(path)

path = "/a//b////c/d//././/.."
assert "/a/b/c" == Solution().simplifyPath(path)

path = "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"
assert "/e/f/g" == Solution().simplifyPath(path)