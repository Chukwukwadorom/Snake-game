from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color):
        self.snake_cells = []
        self.color = color
        self.add(3)

    def add(self,n):
        for x in range(n):
            self.snake_cell = Turtle()
            self.snake_cell.penup()
            self.snake_cell.color(self.color)
            self.snake_cell.shape("square")
            self.snake_cell.goto(-x * 20, 0)
            self.snake_cells.append(self.snake_cell)
        self.head = self.snake_cells[0]

    def move(self):
        for cell in range(len(self.snake_cells) - 1, 0, -1):
            new_x = self.snake_cells[cell - 1].xcor()
            new_y = self.snake_cells[cell - 1].ycor()
            self.snake_cells[cell].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extends(self):
        self.add(1)
        self.move()

    def collide(self):
        for cell in self.snake_cells[1:]:
            if self.head.distance(cell) < 5:
                return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

