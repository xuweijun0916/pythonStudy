# -*- coding: utf-8 -*-
import random
import tkinter


class RandomBall():
    '''
    定义运动的球的类
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        canvas:画布，所有的内容都应该在画布上呈现出来，此处通过此变量传入
        scrnwidth/scrnheight:屏幕宽高
        '''
        # 球出现的初始位置要随机
        # xpos表示位置的x坐标
        self.xpos = random.randint(10, int(scrnwidth) - 20)
        # ypos表示位置的y坐标
        self.ypos = random.randint(10, int(scrnwidth) - 20)
        # 定义球运动的速度
        # 模拟运动：不断的擦掉原来画，然后在一个新的地方再从新绘制
        # 此处xvelocity 模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        # 同理，yvelocity模拟的是y轴方向运动
        self.yvelocity = random.randint(4, 20)
        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        # 定义屏幕的高度
        self.scrnheight = scrnheight
        # 球的大小随机
        # 此处球的大小用半径表示
        self.radius = random.randint(20, 120)

        # 定义颜色
        # RGB表示法：三个数字，每个数字的值是0 - 255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，之间用英文单词表示也可以，比如red, green
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = "#%02x%02x%02x" % (c(), c(), c())

    def creat_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球

        '''
        # tkinter没有画圆形函数
        #  只有一个画椭圆函数，画椭圆需要定义两个坐标
        # 在一个长方形内画椭圆，我们只需要定义长方形左下角和右下角
        # 求两个坐标的方法是，已知圆心的坐标，则圆心坐标减去半径能求出
        # 左上角坐标，加上半径能求出右下角坐标

        x1 = self.xpos - self.radius
    # 继续求y1， x2， y2
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.xpos + self.radius
    # fill表示填充颜色
    # outline是外围边框颜色

    # 在有两个对角坐标的前提下，可以进行画圆
        self.item = self.canvas.creat_oval(x1, y1, x2, y2, fill=self.color ,outline = self.color)



    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        # 同理计算ypos
        self.ypos += self.yvelocity
        # 以下判断是否会撞墙
        # 注意撞墙的算法判断
        if self.xpos + self.radius >= self.scrnwidth:
            # 撞到了右边墙
            self.xvelocity = -self.xvelocity

            # 同理可以判断撞上下左右的墙
        elif self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.xvelocity

        elif self.xpos - self.radius <= 0:
            self.xvelocity = -self.xvelocity
        elif self.ypos - self.radius <= 0:
            self.yvelocity = -self.yvelocity

            # 在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver:
    '''
    定义屏保的类
    可以被启动
    '''
    # 如何装随机产生的球？
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)
        # 同理，按动任何键盘都需要退出屏保
        self.root.bind('<Key>', self.myquit)

        # 得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.cavas, scrnwidth=w, scrnheight=h)
            ball.creat_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

        def run_screen_saver():
            for ball in self.ball:
                ball.move_ball()

            # after是200毫秒后启动一个函数，需要启动的函数是第二个参数
            self.cavas.after(200, self.run_screen_saver)

        def myquit(self, event):
            # 此处只是利用了事件处理机制
            # 实际上并不关心事件类型
            # 作业：
            # 此屏保程序扩展成一旦捕获事件，则判断屏保不退出
            # 显示一个Button,Button上显示事件类型，点击Button后屏保才退出
            self.root.destroy()


if __name__ == "__main__":
    # 启动屏保
   ScreenSaver()

