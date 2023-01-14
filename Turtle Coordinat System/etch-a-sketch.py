from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    return tim.forward(10)


def move_backward():
    return tim.backward(10)


def move_anti_clockwise():
    return tim.left(10)


def move_clockwise():
    return tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_anti_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
