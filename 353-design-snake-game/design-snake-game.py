class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0,0)])
        self.snakeSet = set()
        self.snakeSet.add((0,0))
        self.width = width
        self.height = height
        self.food = food
        self.foodIndex = 0
        self.movement = {'U': (-1, 0), 'L': (0, -1), 'R':(0, 1), 'D': (1,0)}

    def move(self, direction: str) -> int:
        # move the snake in U, D, L, R direction
        # return the gaem score afer the move, -1 if game over
        newHead = (self.snake[0][0] + self.movement[direction][0],
                    self.snake[0][1] + self.movement[direction][1])

        #boundary
        crossesBoundary1 = newHead[0] <0 or newHead[0]>= self.height
        crossesBoundary2 = newHead[1] < 0 or newHead[1] >= self.width

        # check if snake bites itself -> if newHead is the currentTail, it will not bite itself.
        bites = newHead in self.snakeSet and newHead!=self.snake[-1]

        if crossesBoundary1 or crossesBoundary2 or bites:
            return -1
        nextFood = self.food[self.foodIndex] if self.foodIndex < len(self.food) else None

        # if there is food available and it is present on the newHead cell
        if self.foodIndex < len(self.food) and nextFood[0] == newHead[0] and nextFood[1] == newHead[1]:
            self.foodIndex+=1
        else:
            tail = self.snake.pop()
            self.snakeSet.remove(tail)
        
        self.snake.appendleft(newHead)
        self.snakeSet.add(newHead)
        return len(self.snake)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)