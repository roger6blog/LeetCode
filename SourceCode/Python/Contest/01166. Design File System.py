'''

1166. Design File System
Difficulty: Medium
You are asked to design a file system which provides two functions:

create(path, value): Creates a new path and associates a value to it if possible and returns True.
                     Returns False if the path already exists or its parent path doesn't exist.
get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.



Example 1:

Input:
["FileSystem","create","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.create("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input:
["FileSystem","create","create","get","create","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.create("/leet", 1); // return true
fileSystem.create("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.create("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.


Constraints:

The number of calls to the two functions is less than or equal to 10^4 in total.
2 <= path.length <= 100
1 <= value <= 10^9

'''

class FileSystem(object):

    def __init__(self):
        self.fs = {'': 0}

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        parent = path.rsplit('/', 1)[0]
        if parent in self.fs:
            self.fs[path] = value
            return True
        else:
            return False

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        return self.fs.get(path, -1)


path = ["FileSystem","create","get"]
value = [[],["/a",1],["/a"]]

f = FileSystem()
p_1 = f.create("/a/b", 1)
p_2 = f.get("/a")
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)