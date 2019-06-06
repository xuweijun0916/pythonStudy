# -*- coding: utf-8 -*-
import random
from tkinter import *
import threading
import queue
import time


class Food():
    '''
    功能：
        1.出现在画面的某一个地方
        2.一旦被吃，则增加蛇的分数
    '''

    def __init__(self, queue):
        '''
        自动产生一个食物
        '''
        self.queue = queue
        self.new_food()


    def new_food(self):
        '''
        功能：产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        '''
        # 注意横纵坐标产生的范围
        x = random.randrange(5, 480, 10)
        y = random.randrange(5, 295, 10)
        # 同理产生y坐标
        # 需要注意的是，我们的给游戏的屏幕一般不需要设置为正方形

        self.position = x, y  # position存放食物的位置
        self.exppos = x-5, y-5, x+5, y+5

        # 队列，就是一个不能够随意访问内部元素，只能从头弹出一个元素并只能从队尾追加元素的list
        # 把一个食物产生的消息放入队列
        # 消息的格式自己定义
        # 我的定义是：消息是一个dict，k代表消息类型，v代表此类型的数据
        self.queue.put({"food": self.exppos})

class Snake(threading.Thread):
    '''
    蛇的功能：
        1.蛇能动，由我们的上下左右按键控制
        2.蛇每次动，都需要重新计算蛇头的位置
        3.检测是否游戏结束的功能
    '''

    def __init__(self, world, queue):
        threading.Thread.__init__(self)
        self.world = world
        self.queue = queue
        self.point_earned = 0  # 游戏分数
        self.food = Food(self.queue)
        self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]
        self.direction = 'Left'
        self.start()

    def run(self):
        '''
        一旦启用多线程调用此函数
        要求蛇一直跑
        '''
        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.5)  # 蛇的速度
            self.move()

    def move(self):
        '''
        负责蛇的移动
        1.重新计算蛇头的坐标
        2.当蛇头跟食物相遇，则加分，重新生成食物，通知world加分
        3.否则，蛇需要动

        '''
        new_snake_point = self.cal_new_position()  # 重新计算蛇头位置
            # 蛇头位置跟食物位置相同
        if self.food.position == new_snake_point:
            self.point_earned += 1
            self.queue.put({"point_earned": self.point_earned})
            self.food.new_food()  # 就得食物被吃掉，产生新的食物

        else:
                # 需要注意蛇的信息的保存方式
                # 每次移动是删除存放蛇的最前位置，并在后面追加
            self.snake_points.pop(0)
            # 判断程序是否退出，因为新的蛇可能撞墙
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

    def cal_new_position(self):
        '''
        计算新的蛇头的位置
        '''
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":  # direction负责存储蛇移动的方向
            new_snake_point = last_x, last_y - 10  # 每次移动的跨度是10像素
        elif self.direction == 'Down':
            new_snake_point = last_x, last_y + 10
        elif self.direction =='Left':
            new_snake_point = last_x - 10, last_y
        elif self.direction =='Right':
            new_snake_point = last_x + 10, last_y
        return new_snake_point

    def key_pressed(self, event):
            # keysym是按键名称
        self.direction = event.keysym

    def check_game_over(self, snake_point):
        '''
        判断的依据是蛇头是否和墙相撞
        '''
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})

class World(Tk):
    '''
    用来模拟整个游戏画板
    '''

    def __init__(self,queue):
        Tk.__init__(self)

        self.queue = queue
        self.is_game_over = False

            # 定义画板
        self.canvas = Canvas(self, width=500, height=300, bg='red')
        self.canvas.pack()

            # 画出蛇和食物
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill="black", width=10)
        self.food = self.canvas.create_rectangle((0, 0), (0, 0), fill="#FFCC4C", outline="#FFCC4C")
        self.points_earned = self.canvas.create_text((450, 20), fill="white", text="SCORE:0")
        self.queue_handler()

    def queue_handler(self):
        try:
                # 需要不断从消息队列拿到消息，所以死循环
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                if task.get("move"):
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)
                if task.get("food"):
                    self.canvas.coords(self.food, *task['food'])
                if task.get("point_earned"):
                    self.canvas.itemconfigure(self.points_earned, text='score:{}'.format(task['point_earned']))


                    # 同样道理，还需要处理食物，得分
        except queue.Empty:  # 报出队列为空异常
            if not self.is_game_over:
                    # after的含义是，在多少毫秒后调用后面的函数
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        '''
        游戏结束，清理现场
        '''
        self.is_game_over = True
        self.canvas.create_text(220, 150, fill="white",text="Game Over")
        qb = Button(self, text="Quit", command=self.destroy)
        rb = Button(self, text="Again", command=self.restart)
        self.canvas.create_window(230, 180, anchor=W, window=qb)
        self.canvas.create_window(200, 180, anchor=E, window=rb)

    def restart(self):
        self.destroy()
        main()

def main():
    q = queue.Queue()
    world = World(q)
    snake = Snake(world, q)
    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)
    # 同样绑定邮件，上下键
    world.mainloop()
if __name__ == "__main__":
    main()
main()

