import math
'''
# celi() 向上取整操作
print(math.ceil(5.01))

# 查看系统保留关键字，不可以用来当作变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入操作
print(round(5.01))
print(round(5.6))

# sqrt() 开平方 返回浮点数
print(math.sqrt(4))


# pow() 与幂运算差不多，计算一个数的几次方，有两个参数，第一个是底数，第二个是指数
print(math.pow(4,3)) #4的三次方
# 幂运算 函数返回浮点型，幂运算返回整形
print(4**3)


# fabs() 对一个数值获取他的绝对值 返回的也是浮点数
print(math.fabs(-1))
print(math.fabs(3))


# abs() 获取绝对值操作 不是数学模块中的，是Python内置函数,返回值由本身类型而定
print(abs(-1))
print(abs(-2.5))

# fsum() 对整个序列求和
print(math.fsum([2,3,4,5]))
# sum() Python内置求和
print(sum([2,3,4,5]))


# math.modf() 将一个浮点数分为整数部分和小数部分组成元组,小数部分在前，小数部分在后
print(math.modf(4.5))
print(math.modf(0))
help(math.modf)

# copysign() 将第二个数的符号（正负号）传给第一个数
print(math.copysign(2,-3))

# 打印自然对数e和π的值
print(math.e)
print(math.pi)


import random
# random() 获取0-1之间的随机小数，包含0不包含1
for i in range(10):
    # print(random.random())
    # print(random.randint(1,6))
    # random.randrange() 获取指定开始和结束之间的值，可以指定间隔值
    # print(random.randrange(1,9))
    # uniform() 随机获取指定范围内的值（包括小数）
    print(random.uniform(1,9))
    # choice() 随机获取列表中的值
    # print(random.choice([1,5,367,86]))

    # shuffle() 随机打乱序列 返回值是None
    # list1 = [1,5,367,86]
    # print(random.shuffle(list1))

'''

import random
import math

# 输入函数
num = input("请输入一个三位数：")
# 检测输入是否是纯数字
if num.isdigit() and 100<= int(num) <= 999:
    # 输入函数输入的是字符类型，不强制转换会报错
    # 判断输入的数与系统随机数比较大小
     pass
else:
    print("您输入的有误")






