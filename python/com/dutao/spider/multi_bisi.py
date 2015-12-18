'''
Created on 2015-12-17

@author: dutao
'''
import requests
from bs4 import BeautifulSoup
import os
 
s = requests.session()
 
#下载图片
def saveImg(imageURL,fileName):
    try:
        #下载图片设置超时，建立链接3s，下载10s
        data=requests.get(imageURL,timeout=(3,10))
    except:
        return True
    f=open(fileName,"wb")
    f.write(data.content)
    f.close()
 
#建立目录存储每个帖子的图片
def mkdir(path):
    path=path.strip()
    isExist=os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        return True
    else:
        return False
 
#创建目录存储所有帖子
mkdir("img")
os.chdir("img")
 
#模拟登录，请使用正确的帐户和密码
login_data = {'fastloginfield': 'username',
              'username': '爆米那个花',
              "password":"...",
              "quickforward":"yes",
                "handlekey":"ls"
}
r=s.post('http://hk-bici.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1', login_data)
#爬第一页的所有帖子，如果爬第二页修改网址forum-18-2
r = s.get('http://hkbici.com/forum-18-1.html')
soup = BeautifulSoup(r.text,'lxml')
href=[]
for i in soup.find_all("div",class_="c cl"):
    href.append(i.find("a").get("href"))
 
 
dirCount=0
for i in href:
    url="http://hkbici.com/"+i.strip()
    print(url)
    sp=BeautifulSoup(s.get(url).text,'lxml')
    dirCount+=1
    name=str(dirCount)+sp.find("meta",{"name":"keywords"}).get("content").strip()
    mkdir(name)
    count=0
    for m in sp.find_all("ignore_js_op"):
        count+=1
        if m.find("img").get("file"):
            imageURL="http://hkbici.com/"+m.find("img").get("file").strip()
            fileName =name+"/"+str(count)+".jpg"
            saveImg(imageURL,fileName)