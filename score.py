from turtle import Turtle

X_CORD = 0
Y_CORD = 280
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.text = f"Score : {self.score}"
        self.hideturtle()
        self.penup()
        self.goto(X_CORD, Y_CORD)
        self.color("white")
        self.write_score(self.text)

    def update(self):
        self.clear()
        self.score += 1
        self.text = f"Score : {self.score}"
        self.write_score(self.text)

    def game_over(self):
        self.goto(0,0)
        self.write_score("GAME OVER")

    def write_score(self,text):
        self.write(text, align = ALIGN, font = FONT)


