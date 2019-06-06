#!/usr/bin/env python3

#Chapter 11 Project
# lucky.py - Opens several Google search results

import requests
import sys
import webbrowser
import bs4

print('baiduing...') #Display message while retrieving the Google page

# 读取命令行参数sys.argv,使用requests模块获取搜索结果页面
res = requests.get('https://baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 从下载页面的HTML文本创建对象，使用选择器'.ra'查找具有rcss类的元素内的所有元素
soup = bs4.BeautifulSoup(res.text,features='html.parser')
linkElems = soup.select('.r a')

# 打开选项卡的数量为5或者是soup.select('.r a')选择器匹配的所有元素的列表的长度
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://baidu.com' + linkElems[i].get('href'))