import requests
from io import BytesIO
from PIL import Image
import json

'''
print(dir(requests))
url = 'http://www.baidu.com'
r = requests.get(url)
#print(r.text)
#print(r.status_code)
#print(r.encoding)

# 传递参数：比如：http://xxx?aa=bb&cc=dd
params = {'k1':'v1','k2':'v2','k3':[1, 2, 3]}
r = requests.get('http://httpbin.org/get', params)
print(r.url)

# 二进制数据，图片保存
r = requests.get('https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2658838403,155619205&fm=200&gp=0.jpg')
image = Image.open(BytesIO(r.content))
# image.save('1.jpg')

# Json数据
r = requests.get('http://github.com/timeline.json')
print(type(r))
print(r.text)

# 原始数据处理
r = requests.get('https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2658838403,155619205&fm=200&gp=0.jpg')
with open('1.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)


# 提交表单
form ={'username':'user', 'password':'pass'}
r = requests.post('http://httpbin.org/post', data = form)
print(r.text)
r = requests.post('http://httpbin.org/post', data = json.dumps(form))
print(r.text)

# cookie
url = 'http://www.baidu.com'
r = requests.get(url)
cookies = r.cookies
for k, v in cookies.get_dict().items():
    print(k, v)
'''
cookies = {'c1':'v1', 'c2':'v2'}
r = requests.get('http://httpbin.org/cookies', cookies = cookies)
print(r.text)

# 重定向和重定向历史
r = requests.get('http://github.com', allow_redirects = True)
print(r.url)
print(r.status_code)
print(r.history)

# 代理
proxies = {'http://':'', 'https://':''}
r = requests.get('', proxies = proxies)