import turtle

from entity.beans import *

running = True
the_snake = Snake()


def change_dir_u():
    global the_snake
    the_snake.change_dir(Snake.UP)
    pass


def change_dir_d():
    the_snake.change_dir(Snake.DOWN)
    pass


def change_dir_l():
    the_snake.change_dir(Snake.LEFT)
    pass


def change_dir_r():
    the_snake.change_dir(Snake.RIGHT)
    pass


def run():
    global the_snake
    if running:
        the_snake.step_one()
        turtle.ontimer(run, 300)
    pass


def toggle():
    global running
    if running:
        running = False
    elif not running:
        running = True
        run()
    pass


def start_snake():
    turtle.hideturtle()
    the_snake.draw()

    scr = turtle.Screen()
    scr.onclick(the_snake.eat_one, btn=2)
    scr.onclick(the_snake.step_one, btn=1)
    scr.onkey(change_dir_u, key='Up')
    scr.onkey(change_dir_d, key='Down')
    scr.onkey(change_dir_l, key='Left')
    scr.onkey(change_dir_r, key='Right')
    scr.onkey(toggle, key='space')

    run()

    scr.listen()
    turtle.mainloop()
    pass


if __name__ == "__main__":
    start_snake()
    pass
