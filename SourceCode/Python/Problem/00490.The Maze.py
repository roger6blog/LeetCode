'''
Level: Medium  Tag: [DFS]

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by
rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops,
it could choose the next direction.

Given the ball's start position, the destination and the maze,
determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by row and column indexes.

1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures),
    but you could assume the border of the maze are all walls.
5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

Example 1:

Input:
map =
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [3,2]
Output:
false

Example 2:

Input:
map =
[[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [4,4]
Output:
true


'''

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        def valid_dir(maze, x, y):
            if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
                return False
            return True
        visit = set()
        dx = [0, 0, 1, -1]
        dy = [1, -1,0,  0]
        dir = []
        ans = []
        for i in range(len(dx)):
            dir.append([dx[i], dy[i]])

        def dfs(x, y, maze, dest):
            if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
                return False

            if (x, y) in visit:
                return False

            if maze[x][y] == 1:
                return False

            if [x, y] == dest:
                ans.append(True)
                return

            visit.add((x, y))
            for dx, dy in dir:
                new_x = x
                new_y = y
                while valid_dir(maze, new_x+dx, new_y+dy):
                    new_x += dx
                    new_y += dy
                if (new_x, new_y) not in visit:
                    dfs(new_x, new_y, maze, dest)

        dfs(start[0], start[1], map, destination)
        print(ans)
        if not ans:
            return False

        return True

# map = [
#  [0,0,1,0,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [1,1,0,1,1],
#  [0,0,0,0,0]
# ]
# start = [0,4]
# end = [3,2]
# Solution().hasPath(map, start, end)

map = [[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [4,4]
Solution().hasPath(map, start, end)