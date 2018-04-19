import urllib.request
'''
尝试爬取豆瓣排名前250名的电影(post请求模式），获得html文件
'''
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537"}

url="https://movie.douban.com/top250"
for i in range(10):
    formdata={
        "start":i*25,
        "filter":""
    }
    data=urllib.parse.urlencode(formdata).encode('utf-8')   #将字典转为url形式（带&）
    request=urllib.request.Request(url,data=data,headers=headers)
    response=urllib.request.urlopen(request).read().decode("utf-8",'ignore')
    filename="POST-No."+str(i+1)+"Page.html"
    print("正在保存"+filename)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(response)

