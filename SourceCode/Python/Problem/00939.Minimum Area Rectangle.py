'''
Level: Medium

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points,

with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.



Example 1:

"../../../Material/rec1.jpeg"

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

"../../../Material/rec2.jpeg"

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 10^4
All the given points are unique.
'''

class Solution(object):
    # 一樣TLE但是較快
    '''
    为了优化查找的时间, 可以事先把所有具有相同横坐标的点的纵坐标放入到一个 HashSet 中
    使用一个 HashMap, 建立横坐标和所有具有该横坐标的点的纵坐标的集合之间的映射。
    然后开始遍历任意两个点的组合, 由于这两个点必须是对角顶点, 所以其横纵坐标均不能相等, 若有一个相等了, 则跳过该组合。
    否则看其中任意一个点的横坐标对应的集合中是否均包含另一个点的纵坐标, 均包含的话, 说明另两个顶点也是存在的
    就可以计算矩形的面积了
    '''
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        map = defaultdict(list)
        ans = float('inf')
        X = 0
        Y = 1

        n = len(points)
        for x, y in points:
            map[x].append(y)

        for i in range(n):
            for j in range(i+1, n):
                if points[i][X] == points[j][X] or points[i][Y] == points[Y]:
                    continue
                if points[j][Y] in map[points[i][X]] and points[i][Y] in map[points[j][X]]:
                    area = abs(points[i][X]-points[j][X]) * abs(points[i][Y]-points[j][Y])
                    if area != 0:
                        ans = min(ans, area)

        print(ans)
        if ans == float('inf'):
            return 0

        return ans


    def minAreaRect_TLE(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = float('inf')
        X = 0
        Y = 1
        points.sort()
        n = len(points)
        for i in range(n):
            j = i + 1
            while j < n:
                # 找出同X座標的第二點
                if points[i][X] != points[j][X]:
                    j += 1
                    continue
                height1 = points[j][Y] - points[i][Y]
                if height1 == 0:
                    # 等高的Y不能當第二點
                    continue

                # 找出跟height1等高的height2
                # 和第一點同Ｙ座標的第三點
                for k in range(i+1, n):
                    if points[k][Y] != points[i][Y]:
                        continue

                    width = points[k][X] - points[i][X]
                    if width == 0:
                        continue

                    height2 = 0
                    q = k + 1
                    # 找出和第三點同Ｘ座標的第四點
                    while q < n:
                        if points[q][X] != points[k][X]:
                            q += 1
                            continue
                        height2 = points[q][Y] - points[k][Y]

                        if height2 == 0 or height2 != height1:
                            q += 1
                            continue


                        ans = min(ans, width*height1)
                        break
                j += 1

        print(ans)
        if ans == float('inf'):
            return 0

        return ans

points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Solution().minAreaRect(points)

points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Solution().minAreaRect(points)