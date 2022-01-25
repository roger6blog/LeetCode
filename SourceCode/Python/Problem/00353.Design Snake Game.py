'''
Level: Medium   Tag: [Design]

Design a Snake game that is played on a device with screen size = width x height.

Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order.

When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen.

For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen,
it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1
(Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)

Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


'''
from collections import deque
class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """

        self.x = height
        self.y = width
        self.board = [[0] * width for _ in range(height)]
        self.food_queue = deque(food)
        self.food = self.food_queue.popleft()
        self.snake_len = 1
        self.snake = deque()
        self.snake.append((0,0))


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        curr = self.snake[-1]
        x, y = curr[0], curr[1]
        if direction == 'U':
            x -= 1
        if direction == 'D':
            x += 1
        if direction == 'R':
            y += 1
        if direction == 'L':
            y -= 1

        if x >= self.x or x < 0 or y < 0 or y >= self.y:
            print("Snake hit the boarder, game over")
            return -1

        if (x, y) in self.snake:
            print("Snake ate its body, game over")
            return -1

        if [x, y] == self.food:
            print("Snake got food, yummy~~~~!!")
            self.snake_len += 1
            if self.food_queue:
                self.food = self.food_queue.popleft()

        self.snake.append((x, y))
        while len(self.snake) > self.snake_len:
            self.snake.popleft()








# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


width = 3
height = 2
food = [[1,2],[0,1]]
obj = SnakeGame(width, height, food)
print(obj.move('R'))
print(obj.move('D'))
print(obj.move('R'))
print(obj.move('U'))
print(obj.move('L'))
print(obj.move('U'))