import random
import math

'''
输入一个三位数与程序随机数比较大小
1.如果大于程序随机数，则输出这个三位数的个位\十位\百位
2.如果等于程序随机数，则提示中奖，记100分
3.如果小于程序随机数，则将120个字符输入到文本文件
（规则是每一条字符串的长度为12，单独占一行，并且前4个是字母，后八个是数字）
'''
class GameNum():
    def line(self):
        # 定义一个空字符串用于拼接字符
        str_num = ''

        # 循环前4个随机字母（用accii对应的值来随机在转化为字母)
        for i in range(4):
            # 随机小写字母的ascii值
            num = random.randrange(97,123)
            # 将ascii值转换成对应的字母
            str_s = chr(num)
            # 依次拼接得到的随机字母
            str_num = str_num + str_s
        #print(str_num)
        # 循环后八个随机数字
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num + str(num)
        #print(str_num)
        return str_num


    sourse = 0
    #输入函数
    num = input("请输入一个三位数：")
    # 程序随机数
    random_num = random.randrange(100,1000)
    #检测输入是否是纯数字
    if num.isdigit() and 100<=int(num) <=999:
        num = int(num)
        # 判断随机数与输入数的大小
        if num > random_num:
            # 求百位数字方法是地板除100或用数学模块当中的floor（）函数
            # bai = num // 100
            # 求十位数字的方法是先把三位数取100的余数，再地板除
            # shi = num % 100 // 10
            # 求个位数字方法是直接取10的模
            # ge = num % 10
            print("你输入的数比程序随机数大，程序随机数是",random_num)
            print("你输入的三位数百位是{}, 十位是{}, 个位是{}".format(num//100,num%100//10,num%10))
        if num == random_num:
            sourse = sourse + 100
            print('你中奖了，目前分数为',sourse)
        if num < random_num:
            # 由于120个字符每行2个，可知只需存入10行即可
            for i in range(10):
                str_line = line()
                #print(str_line)
                # 执行文件存入操作
                with open('str_num.txt','a') as f:
                    f.write(str_line)
    else:
        print("请输入规定的输入")


if __name__ == '__main__':
    # 在本身模块中__name__ == __main__ ,当第三方导入的时候__name__ == 文件名
    # 定义一个变量用于存取初始分数
    sourse = 0
    # 定义一个变量用于累计输入多少次
    total = 0
    GameNum.num_game(sourse,total)