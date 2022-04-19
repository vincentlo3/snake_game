from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def tail_collision(self):
        for segment in self.segments[2:]:
            if self.head.distance(segment) < 20:
                return True

    def move(self):
        for num_segment in range(len(self.segments) - 1, 0, -1):
            if -280 < self.head.xcor() < 280 and -280 < self.head.ycor() < 280:
                new_position = self.segments[num_segment - 1].position()
                self.segments[num_segment].setposition(new_position)
            else:
                return False
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
