import urllib

if __name__ == '__main__':
    url = 'http://stock.eastmoney.com/news/1407,20170807763593890.html'
    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{}".format(rsp.info()))
    print("Code:{}".format(rsp.getcode()))
    html = rsp.read()
    #print(html)
