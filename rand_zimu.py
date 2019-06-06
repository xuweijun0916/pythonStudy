class GameZiMu():
    # 打印字母A
    # 控制行
    def A(self):
        for i in range(1,5):
            # 判断开始输入的位置
            for k in range(5-i):
                print(' ', end="")
            # 控制列
            for j in range(1,i+1):
                if i == 1  or j == 1 or j == i:
                    print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母B
    def B(self):
        for i in range(1, 4):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # 字母D
    def D(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # 字母C
    def C(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i==1 or i==4:
                    if j==1:
                        print(' ',end=' ')
                    else:
                        print('*',end=' ')
                elif j==1:
                    if i==2 or i==3:
                        print('*',end="")
                else:
                    print(" ", end=" ")
            print()

    # 打印字母E
    def E(self):
        for m in range(1,7):
            for n in range(1,4):
                if m==1 or m==4 or m==6 or n==1:
                    print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母E
    def F(self):
        for m in range(1,7):
            for n in range(1,4):
                if m==1 or m==4  or n==1:
                    print('*', end=" ")
                else:
                    print(' ',end=" ")
            print()

    # 打印字母G
    def G(self):
        for m in range(1,5):
            for n in range(1,5):
                if m==1 or m==4 :
                    if n==1:
                        print(" ", end=" ")
                    else:
                        print("*",end=" ")
                elif m == 2 and n==1:
                    print("*", end=" ")
                elif m == 3:
                    if n == 2:
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")

                else:
                    print(' ',end=" ")
            print()

    # 打印字母J
    def J(self):
        for m in range(1,6):
            for n in range(1,5):
                if m==1 or n==3:
                    if m<5:
                        print("*", end=" ")
                elif m==4 and n==1:
                    print("*", end=" ")
                elif m==5 and n==2:
                    print("*", end=" ")
                else:
                    print(" ",end=" ")
            print()

    # 打印字母K
    def K(self):
        for m in range(1,3):
            for n in range(m,4):
                if m==1 and n==2 :
                    print(" ",end=" ")
                else:
                    print("*",end=" ")
            print()
        for m in range(1,4):
            for n in range(m):
                if n==0 or n==m-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    # 打印字母M
    def M(self):
        for i in range(1, 5):
            # 判断开始输入的位置
            for k in range(5 - i):
                print(' ', end="")
            # 控制列
            for j in range(1, i + 1):
                if i == 1 or j == 1 or j == i:
                    print('*', end=" ")
                else:
                    print(' ', end=" ")
            print()
        for i in range(1, 5):
            # 判断开始输入的位置
            for k in range(5 - i):
                print(' ', end="")
            # 控制列
            for j in range(1, i + 1):
                if i == 1 or j == 1 or j == i:
                    print('*', end=" ")
                else:
                    print(' ', end=" ")
            print()

    # 打印字母N
    def N(self):
        for m in range(1,5):
            for n in range(1,5):
                if n==1 or n==4 or m==n:
                    print("*", end=" ")
                else:
                    print(" ",end=" ")
            print()

