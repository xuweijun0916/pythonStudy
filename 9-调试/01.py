def SayHello(name):
    print("I want to say hello with you {}".format(name))
    print("Hello,{}".format(name))
    print("Done....")

if __name__ == "__main__":
    print('***' * 10)
    name = input("please input your name: ")
    print(SayHello(name=name))
    print('@@@' * 10)