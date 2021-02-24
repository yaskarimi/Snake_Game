from turtle import Turtle

STARATING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
Up = 90
DOWN = 270
LEFT = 180
RIGHT =0

class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]
    def create(self):

        for i in STARATING_POSITIONS:
            self.add_seg(i)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x , new_y)
        self.segments[0].forward(20)


    def add_seg(self,position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):

        self.add_seg(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(Up)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(DOWN)
