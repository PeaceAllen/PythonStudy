import random
import turtle


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


'''
贪吃蛇object
'''


class Snake:
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

    def __init__(self):

        self.block_size = 14
        self.margin = 2

        # 当前运行方向,0: +x, 1: -x, 2: +y, 3: -y
        self.direction = 0

        # 当前所有的方块
        self.blocks = [Point()]

        self.random = random.Random()
        self.food_block = Point()
        self.generate_food()

        pass

    def step_one(self):
        new_block = self.create_new_block()
        size = len(self.blocks)
        print("size - %d" % (size))
        self.blocks.remove(self.blocks[size - 1])
        self.blocks.insert(0, new_block)

        if self.in_block_rect(self.blocks[0].x, self.blocks[0].y, self.food_block):
            self.generate_food()
            self.add_one_block()

        self.draw()
        pass

    def create_new_block(self):
        head_block = self.blocks[0]
        x = 0
        y = 0
        if self.direction == 0:
            x = head_block.x + (self.block_size + self.margin)
            y = head_block.y
        elif self.direction == 1:
            x = head_block.x - (self.block_size + self.margin)
            y = head_block.y
        elif self.direction == 2:
            y = head_block.y + (self.block_size + self.margin)
            x = head_block.x
        elif self.direction == 3:
            y = head_block.y - (self.block_size + self.margin)
            x = head_block.x
        return Point(x, y)

    def add_one_block(self):
        new_block = self.create_new_block()
        self.blocks.insert(0, new_block)
        self.print_all_blocks()
        pass

    def print_all_blocks(self):
        for i in range(len(self.blocks)):
            print("block: %d, %d" % (self.blocks[i].x, self.blocks[i].y))
        pass

    def change_dir(self, new_dir):
        self.direction = new_dir
        self.step_one()
        self.draw()
        pass

    def draw_one_block(self, pos: Point, index=0, is_food=False):
        turtle.tracer(False)
        turtle.up()
        turtle.goto(pos.x, pos.y)
        turtle.down()
        if is_food:
            turtle.fillcolor("red")
        else:
            turtle.fillcolor("black")

        turtle.begin_fill()
        for i in range(4):
            turtle.seth(i * 90)
            turtle.fd(self.block_size)
            pass
        #turtle.write("%d" % (index))
        turtle.end_fill()
        pass

    def draw(self):
        print("size of blocks = %d" % (len(self.blocks)))
        turtle.clear()
        for i in range(len(self.blocks)):
            self.draw_one_block(self.blocks[i], i)

        if self.food_block.x < 10001:
            self.draw_one_block(self.food_block, is_food=True)
            pass

        turtle.update()
        pass

    def eat_one(self, x, y):
        self.add_one_block()
        self.draw()
        pass

    def generate_food(self):

        scr_size = turtle.screensize()

        while True:
            x = self.random.randint(-scr_size[0], scr_size[0])
            y = self.random.randint(-scr_size[1], scr_size[1])
            if self.check_block(x, y) == False:
                self.food_block.x = x
                self.food_block.y = y
                break
        pass

    def check_block(self, x, y):

        conflict = False

        for i in range(len(self.blocks)):
            p = self.blocks[i]
            if self.in_block_rect(x, y, p):
                conflict = True
                break
            pass
        return conflict

    def in_block_rect(self, x, y, block: Point):
        p = block
        tmp = self.block_size + self.margin
        return p.x <= x <= p.x + tmp and p.y <= y <= p.y + tmp
