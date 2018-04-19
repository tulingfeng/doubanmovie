import urllib.request
'''
尝试爬取豆瓣排名前250名的电影(get请求模式）,获得html文件
'''
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537"}

for i in range(10):
    url="https://movie.douban.com/top250?start={}&filter=".format(i*25)
    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request).read().decode("utf-8",'ignore')
    filename="No."+str(i+1)+"Page.html"
    print("正在保存"+filename)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(response)

