import requests
import re
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
# from requests_oauthlib import OAuth1
from requests import Request, Session





# # get请求
# r = requests.get('https://static1.scrape.center/')
# print(r.text)

#get请求带参数并且解析返回值为JSON
# data = {
#     'name': 'germey',
#     'age': 25
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

#抓取title
# r = requests.get('https://static1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


#抓取图片
# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

#添加 headers
# import requests
#
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://static1.scrape.center/', headers=headers)
# print(r.text)


#POST 请求

# import requests
#
# data = {'name': 'germey', 'age': '25'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)

#响应
# import requests
#
# r = requests.get('https://static1.scrape.center/')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)


#内置状态码requests.codes
# r = requests.get('https://static1.scrape.center/')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')


#文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)


#获取和设置Cookies

# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
#
# headers = {
#     'Cookie': '_octo=GH1.1.1849343058.1576602081; _ga=GA1.2.90460451.1576602111; __Host-user_session_same_site=nbDv62kHNjp4N5KyQNYZ208waeqsmNgxFnFC88rnV7gTYQw_; _device_id=a7ca73be0e8f1a81d1e2ebb5349f9075; user_session=nbDv62kHNjp4N5KyQNYZ208waeqsmNgxFnFC88rnV7gTYQw_; logged_in=yes; dotcom_user=Germey; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; _gh_sess=your_session_info',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# r = requests.get('https://github.com/', headers=headers)
# print(r.text)

#Session 维持
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


#SSL 证书验证
#logging.captureWarnings(True)  #捕获警告到日志的方式忽略警告：
# urllib3.disable_warnings()  #忽略警告
# response = requests.get('https://static2.scrape.center/', verify=False)
# print(response.status_code)

#response = requests.get('https://static2.scrape.center/', cert=('/path/server.crt', '/path/server.key'))  #也可以指定一个本地证书用作客户端证书

#超时设置
# r = requests.get('https://httpbin.org/get', timeout=1)
# print(r.status_code)
# #实际上，请求分为两个阶段，即连接（connect）和读取（read）。上面设置的 timeout 将用作连接和读取这二者的 timeout 总和。如果要分别指定，就可以传入一个元组：
# r = requests.get('https://httpbin.org/get', timeout=(5, 30))

#身份认证
# r = requests.get('https://static3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# #r = requests.get('https://static3.scrape.center/', auth=('admin', 'admin')) 简写
# print(r.status_code)


#OAuth 认证
#pip3 install requests_oauthlib
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)


#代理设置
# proxies = {
#   'http': 'http://10.10.10.10:1080',
#   'https': 'http://10.10.10.10:1080',
# }
# requests.get('https://httpbin.org/get', proxies=proxies)
#
# #代理 + 身份认证
#
# proxies = {'https': 'http://user:password@10.10.10.10:1080/',}
# requests.get('https://httpbin.org/get', proxies=proxies)

#除了基本的 HTTP 代理外，requests 还支持 SOCKS 协议的代理。
#pip3 install "requests[socks]"

# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get('https://httpbin.org/get', proxies=proxies)

#Prepared Request
url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)