'''
Created on 2015-12-16

@author: dutao
'''
import re
from urllib import request
from collections import deque

queue = deque()
visited = set()

num = 0
index_url = 'http://www.saqw.cn/7.html'
queue.append(index_url)

while queue:
    url = queue.popleft()
    visited.add(url)  # 标记为已访问
    
    print('已抓取'+str(num)+'个网页，正在抓取'+url)
    num += 1
    
    req = request.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })   
    response = request.urlopen(req)
    
    if 'html' not in response.getheader('Content-Type'):
        continue
    
    try:
        data = response.read().decode()
    except:
        continue    
    
    linkre = re.compile('href="(.+?)"')
    
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
    
    