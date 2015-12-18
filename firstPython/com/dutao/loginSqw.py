'''
Created on 2015-12-16
登录撒钱网
@author: dutao
'''
from urllib import request,parse
import gzip
import http.cookiejar

header = {
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive'          
}

def getOpener(head):
    cookiejar = http.cookiejar.CookieJar()
    processor = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(processor)
    
    header = []
    for k,v in head.items():
        ele = (k,v)
        header.append(ele)
    opener.addheaders = header
    return opener


def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


url = 'http://www.saqw.cn/zb_system/cmd.php?act=verify'
data = {
   'username':'lovetaotao', 
   'password':'57d05f9499c4df76fea4c5a66386cfc7', 
   'savedate':'0', 
   'dishtml5':'0', 
}
opener = getOpener(header)
postData = parse.urlencode(data).encode(encoding='utf_8', errors='strict')
response = opener.open(url, postData)
print(ungzip(response.read().decode('utf_8')))
    
    