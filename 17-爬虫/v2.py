'''
利用request下载页面
自动检测页面编码
'''

import urllib
import chardet

if __name__ == '__main__':
    url = 'http://stock.eastmoney.com/news/1407,20170807763593890.html'
    rsp = urllib.request.urlopen(url)
    html = rsp.read()
    html = html.decode()
    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)
