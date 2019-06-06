'''
movies = ["the holy grail", "the life of brian", "the meaning of life"]
movies.insert(1,1975)
movies.insert(3,1979)
#movies.insert(5,1983)
movies.append(1983)
print(movies)


fav_movies = ["The Holy Grail","The Life of Brian"]
#print(fav_movies[0])
#print(fav_movies[1])

#for each_flick in fav_movies:
#    print(each_flick)

count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count = count + 1
'''

'''
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["John Cleese", "terry Gilliam", "eric Idle", "Terry Jones"]]]
#print(movies)
'''
'''
这是“nester.py”模块，提供了一个名为print_lol()的函数，
这个函数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表。
'''
import sys
def print_lol(the_list,indent = False, level=0, fn = sys.stdout):
    '''
    这个函数取一个位置参数，名为“the_list”,这可以是任何Python列表（也可以是包含嵌套列表的列表）。
    所指定的列表中的每一个数据项会（递归地）输出到屏幕上，各数据项各占一行。
    level参数用来表示列表中每一个层级缩进多少个Tab
    indent参数用来表示层级是否缩进
    fn参数用来标识把数据写入哪个位置，默认输出至屏幕
    '''
    for each_item in the_list:
        if isinstance(each_item ,list):
            print_lol(each_item,indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="", file = fn)
            print(each_item, file = fn)

#print_lol(movies,0)
