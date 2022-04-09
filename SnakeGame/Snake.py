from turtle import Turtle
class Snake:
    def __init__(self):
        self.x_coordinate= 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in range(4):
            self.add_segment(position)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[seg - 1].ycor()
            new_x = self.segments[seg - 1].xcor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(10)


    def move_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(self.x_coordinate, 0)
        self.x_coordinate -= 20
        self.segments.append(segment)