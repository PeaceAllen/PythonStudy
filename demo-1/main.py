import turtle
from turtle import *

from common import initializer
from tanchishe import Block

blocks_size = 10
blocks_margin = 2
blocks = []
tmp_block = Block.Block(0, 0, 0, 0)
moving = False


def init_tcs(count):
    for i in range(count):
        x = i * (blocks_size + blocks_margin)
        y = blocks_size + blocks_margin

        b = Block.Block(x, y, blocks_size, blocks_margin)
        blocks.append(b)
        pass
    pass


def draw_blocks():

    clear()
    for i in range(len(blocks)):
        blocks[i].draw()
    update()

    pass


"""
0: right, 1: up, 2: left, 3: down
"""


def move(dir):
    count = len(blocks)

    tmp_block.x = blocks[0].x
    tmp_block.y = blocks[0].y
    tmp_block.size = blocks[0].size
    tmp_block.margin = blocks[0].margin

    for i in range(1, count):
        blocks[count - i].x = blocks[count - i - 1].x
        blocks[count - i].y = blocks[count - i - 1].y
        blocks[count - i].size = blocks[count - i - 1].size
        blocks[count - i].margin = blocks[count - i - 1].margin
        pass

    if dir == 0:
        blocks[0].x = tmp_block.x + (tmp_block.size + tmp_block.margin)
    elif dir == 1:
        blocks[0].x = tmp_block.x - (tmp_block.size + tmp_block.margin)
    elif dir == 2:
        blocks[0].y = tmp_block.y + (tmp_block.size + tmp_block.margin)
    elif dir == 3:
        blocks[0].y = tmp_block.y - (tmp_block.size + tmp_block.margin)

    draw_blocks()
    pass


def cur_dir():
    x0 = blocks[0].x
    y0 = blocks[0].y
    x1 = blocks[1].x
    y1 = blocks[1].y
    # right
    if x0 > x1 and y0 == y1:
        return 0
    # left
    elif x0 < x1 and y0 == y1:
        return 1
    # up
    elif y0 > y1 and x0 == x1:
        return 2
    # down
    elif y0 < y1 and x0 == x1:
        return 3
    pass


def start():
    global moving
    if moving:
        move(cur_dir())
        ontimer(start, 200)
        pass


def on_start(x, y):
    global moving
    if x > 10:
        moving = True
        ontimer(start, 200)
    elif x < -10:
        moving = False
    print("x = {}, start = {}".format(x, moving))


def test():
    print("hello")
    pass


def main():
    initializer.init(400, 400, 'gray')
    tracer(False)
    init_tcs(3)
    draw_blocks()
    onscreenclick(on_start)

    mainloop()



if __name__ == '__main__':
    # main()
    pass

