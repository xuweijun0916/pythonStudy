# 第一步：画出图形界面上半部
from tkinter import *
import re
import tkinter
import tkinter.messagebox
root = Tk()
# 定义面板的大小
root.geometry('250x380')
root.title('北京图灵学院')

# 放置用来显示信息的文本框，并设置为只读
contentVar = tkinter.StringVar(root,'')
contentEntry = tkinter.Entry(root, textvariable=contentVar)
contentEntry.place(x=10, y=10, width=280, height=20)


# 定义面板
# bg代表背景颜色（background）,#dddddd是十六进制表示颜色的一个串
frame_show = Frame(width=300, height=150, bg='#dddddd')

# 定义顶部区域
sv = StringVar()
sv.set('0')

# anchor:定义控件的锚点，e代表右边
# font代表字体
show_label = Label(frame_show, textvariable=sv, bg='white', width=12, height=1, font=('黑体', 20, 'bold'), justify=LEFT,
                   anchor='e')
show_label.pack(padx=10, pady=10)
frame_show.pack()

# 第二步：画出图形界面下半部分
# 按键区域
frame_bord = Frame(width=400, height=350, bg="#cccccc")


def delete():
    print("删除了")


def fan():
    pass


def clear():
    pass


b_del = Button(frame_bord, text="←", width=5, height=1, command=delete)
b_del.grid(row=0, column=0)
button_clear = Button(frame_bord, text='C', width=5, height=1, command=clear).grid(row=0, column=1)
button_fan = Button(frame_bord, text='±', width=5, height=1, command=fan).grid(row=0, column=2)
button_ce = Button(frame_bord, text='CE', width=5, height=1, command=clear).grid(row=0, column=3)

'''
考虑以下几种情况：
1.按下数字
2.按下操作符号
3.只考虑两个操作数操作，不考虑复杂情况
'''
num1 = 0
num2 = 0
operator = None

def change(num):
    '''
    按下一个数字需要考虑两种情况：
    1.数字属于第一个操作数
    2.数字属于第二个操作数
    3.判断是否属于第一个操作数，可以通过operator判断
    '''
    # 假如操作数是None，表明肯定是第一个操作数
    if not operator:
        num1 = num1 + num
        # 如果是第一个操作数，则只显示第一个操作符
        sv.set(num1)
    else:
        num2 = num2 + num
        # 如果是第二个操作数，则显示完整的计算式子
        sv.set(num1 + operator + num2)


def operation(op):
    if op in ['+', '-', 'x', '/']:
        operation = op
    else:
        # 认为按下的是等号
        if op == '+':
            rst = int(num1) + int(num2)
        if op == '-':
            rst = int(num1) - int(num2)
        if op == 'x':
            rst = int(num1) * int(num2)
        if op == '/':
            rst = int(num1) / int(num2)
    sv.set(str(rst))


def operation(op):
    print(op)


b_1 = Button(frame_bord, text='1', width=5, height=2, command=lambda: change("1"))
b_1.grid(row=1, column=0)

b_2 = Button(frame_bord, text='2', width=5, height=2, command=lambda: change("2"))
b_2.grid(row=1, column=1)

b_3 = Button(frame_bord, text='3', width=5, height=2, command=lambda: change("3"))
b_3.grid(row=1, column=2)

b_4 = Button(frame_bord, text='4', width=5, height=2, command=lambda: change("4"))
b_4.grid(row=1, column=3)

b_5 = Button(frame_bord, text='5', width=5, height=2, command=lambda: change("5"))
b_5.grid(row=2, column=0)

b_6 = Button(frame_bord, text='6', width=5, height=2, command=lambda: change("6"))
b_6.grid(row=2, column=1)

b_7 = Button(frame_bord, text='7', width=5, height=2, command=lambda: change("7"))
b_7.grid(row=2, column=2)

b_8 = Button(frame_bord, text='5', width=5, height=2, command=lambda: change("8"))
b_8.grid(row=2, column=3)

b_9 = Button(frame_bord, text='9', width=5, height=2, command=lambda: change("9"))
b_9.grid(row=3, column=0)

b_0 = Button(frame_bord, text='0', width=5, height=2, command=lambda: change("0"))
b_0.grid(row=3, column=1)

b_plus = Button(frame_bord, text='+', width=5, height=2, command=lambda: operation("+"))
b_plus.grid(row=3, column=2)

b_minus = Button(frame_bord, text='-', width=5, height=2, command=lambda: operation("-"))
b_minus.grid(row=3, column=3)

b_ride = Button(frame_bord, text='x', width=5, height=2, command=lambda: operation("x"))
b_ride.grid(row=4, column=1)

b_divide = Button(frame_bord, text='/', width=5, height=2, command=lambda: operation("/"))
b_divide.grid(row=4, column=2)

frame_bord.pack(padx=10, pady=10)
root.mainloop()