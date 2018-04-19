import urllib.request
import re
'''
爬取豆瓣电影前100名
'''
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537"}

def main():
    url="https://movie.douban.com/top250"
    top_num=1
    temp_data = []
    find_title(url,top_num,temp_data)
    printTxt()
    write(temp_data)
    print("写入结束")

def find_title(url,top_num,temp_data):
    for i in range(4):
        formdata={
             "start":i*25,
            "filter":""
         }
        data=urllib.parse.urlencode(formdata).encode('utf-8')   #将字典转为url形式（带&）
        request=urllib.request.Request(url,data=data,headers=headers)
        response=urllib.request.urlopen(request).read().decode('utf-8')
        # 采用正则
        movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', response, re.S)
        for index, item in enumerate(movie_items):
         # 查找不到返回-1
            if item.find("&nbsp") == -1:
                temp_data.append("Top" + str(top_num) + " " + item)
                top_num += 1

def write(temp_data):
    file=open('movie_top100.txt','w+')
    print("正在写入...")
    file.write("="*30+"\n")
    file.write("一个简单的豆瓣电影前100爬虫"+"\n"+"Author:tutu"+"\n")
    file.write("="*30+"\n")
    for item in temp_data:
        file.write(item+"\n")
    file.close()

def printTxt():
    print("="*30)
    print('一个简单的豆瓣电影前100爬虫')
    print('Author: tutu')
    print("="*30)

if __name__ == "__main__":
    main()



