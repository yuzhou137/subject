<<<<<<< HEAD
#获得内容
# import urllib.request
#
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.status)
# print(type(response))
# print(response.getheader('Server'))

#post 带参数的
import urllib.request
import urllib.parse
#
# data =bytes( urllib.parse.urlencode({'name': 'germey'}),encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

#request相关
# import urllib.request
#
# request = urllib.request.Request('https://www.baidu.com') #data,method,headers,origin_req_host
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 验证
# from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# from urllib.error import URLError
# username = 'admin'
# password = 'admin'
# url = 'https://ssr3.scrape.center'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
# filename = 'result.html'
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     with open (filename,'w',encoding='utf-8') as file:
#         file.write(html)
#     print(f'Successfully write {filename}')
# except URLError as e:
#     print(e.reason)


# cookie
# 获取cookie
# import http.cookiejar,urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard = True,ignore_expires=True)
# 读取并使用cookie
# import urllib.request ,http.cookiejar
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))


# url的分段与读取
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/s?wd=%E4%B8%BA%E4%BB%80%E4%B9%88%E8%AF%B4%E6%9D%AD%E5%B7%9E%E6%8A%9B%E4%B8%8B%E4%B8%96%E7%95%8C%E8%87%AA%E5%B7%B1%E8%BF%9B%E5%8C%96&rsv_spt=1&rsv_iqid=0xb060fa60001721a6&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=ts_1&rsv_enter=1&rsv_sug3=11&rsv_sug1=7&rsv_sug7=100&rsv_sug2=1&rsv_btype=t&prefixsug=%25E4%25B8%25BA%25E4%25BB%2580%25E4%25B9%2588&rsp=1&inputT=3993&rsv_sug4=4932')
print(type(result))
=======
#获得内容
# import urllib.request
#
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.status)
# print(type(response))
# print(response.getheader('Server'))

#post 带参数的
import urllib.request
import urllib.parse
#
# data =bytes( urllib.parse.urlencode({'name': 'germey'}),encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

#request相关
# import urllib.request
#
# request = urllib.request.Request('https://www.baidu.com') #data,method,headers,origin_req_host
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 验证
# from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# from urllib.error import URLError
# username = 'admin'
# password = 'admin'
# url = 'https://ssr3.scrape.center'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
# filename = 'result.html'
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     with open (filename,'w',encoding='utf-8') as file:
#         file.write(html)
#     print(f'Successfully write {filename}')
# except URLError as e:
#     print(e.reason)


# cookie
# 获取cookie
# import http.cookiejar,urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard = True,ignore_expires=True)
# 读取并使用cookie
# import urllib.request ,http.cookiejar
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))


# url的分段与读取
from urllib.parse import urlparse
result = urlparse('https://www.baidu.com/s?wd=%E4%B8%BA%E4%BB%80%E4%B9%88%E8%AF%B4%E6%9D%AD%E5%B7%9E%E6%8A%9B%E4%B8%8B%E4%B8%96%E7%95%8C%E8%87%AA%E5%B7%B1%E8%BF%9B%E5%8C%96&rsv_spt=1&rsv_iqid=0xb060fa60001721a6&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=ts_1&rsv_enter=1&rsv_sug3=11&rsv_sug1=7&rsv_sug7=100&rsv_sug2=1&rsv_btype=t&prefixsug=%25E4%25B8%25BA%25E4%25BB%2580%25E4%25B9%2588&rsp=1&inputT=3993&rsv_sug4=4932')
print(type(result))
>>>>>>> 57fe6b7a40858ab9697896513bc199f264a51c7f
print(result)