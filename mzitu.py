# encoding=UTF-8
import requests
import os
from bs4 import BeautifulSoup

url='http://www.mzitu.com/all'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
r=requests.get(url=url,headers=headers)
soup=BeautifulSoup(r.text,'lxml')#将主页面Beautifulsoup对象化
all_a=soup.find('div',class_='all').find_all('a')#在主页面找到属性为all的所有内容里面的a标签，并形成一个列表
for list in all_a:
        text=list.get_text()#获得该美女名字
        path = str(text).strip()#去掉字符串空格
        os.makedirs(os.path.join('/Users/zhangshuaizhen/Desktop/new',path))
        os.chdir('/Users/zhangshuaizhen/Desktop/new/'+path)
        #创建文件夹
        a=list['href']#提取每一个美女的第一个链接
        #print(text,a)
        url_1=a
        r_1=requests.get(url=url_1,headers=headers)
        soup_1=BeautifulSoup(r_1.text,'lxml')
        lastpage=soup_1.find('div',class_='pagenavi').find_all('span')[-2].get_text()#找到最后一页的页码
        #print (lastpage)
        for page in range(1,int(lastpage)+1):
                page_url=url_1+'/'+str(page)
                r_2=requests.get(url=page_url,headers=headers)
                soup_2=BeautifulSoup(r_2.text,'lxml')
                image_url=soup_2.find('img')['src']
                name=image_url[-9:-4]
                image=requests.get(url=image_url,headers=headers)
                f=open(name+'.jpg','ab')
                f.write(image.content)
                f.close

#done
