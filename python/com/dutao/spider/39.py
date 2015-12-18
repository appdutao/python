'''
Created on 2015-12-17

@author: dutao
'''
import requests
from bs4 import BeautifulSoup
import os
import re
 
s = requests.session()
 
def saveImg(imageURL,fileName):
    try:
        data=requests.get(imageURL,timeout=(3,10))
    except:
        return True
    with open(fileName,"wb") as f:
        f.write(data.content)
    
def saveTxt(txt,fileName):
    with open(fileName,"w",encoding="utf-8") as f:
        f.write(txt)
 
def mkdir(path):
    path=path.strip()
    isExist=os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        return True
    else:
        return False
 
mkdir("39")
os.chdir("39")

index_url = 'http://jianfei.39.net/'

r = s.get('http://jianfei.39.net/bbs')
soup = BeautifulSoup(r.text,'lxml')
href=[]
visited = set()
ul = soup.find("ul",id="gehang")
for a in ul.find_all("a"):
    if a.get('target') == '_blank':
        thread_url = a.get('href')
        thread_url = re.search(r"thread-[0-9]{7}-1.html", thread_url)
        if thread_url:
            visit_url = index_url + thread_url.group(0)
            if  visit_url not in visited:
                href.append(visit_url)
                visited = visited | {visit_url}
            
 
 
dirCount=0
for i in href:
    url=i.strip()
    print(url)
    r = s.get(url)
    r.encoding
    sp=BeautifulSoup(r.text,'lxml')
    dirCount+=1
    name = str(dirCount)
    title = sp.find(id='thread_subject').string
    #print(title)
    #name=str(dirCount)+sp.find("meta",{"name":"keywords"}).get("content").strip()
    #mkdir(name)
    count=1
    td = sp.find_all("td",class_="t_f")
    for nr in td:
        print(str(count) + 'L-------------------------------------------'+title+'-----------------------------------------------------------')
        print(nr.text)
        count = count + 1
        saveTxt(nr.text,name+'.txt')

