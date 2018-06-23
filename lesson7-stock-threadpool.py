import threadpool
import requests
import time

a = time.time()
def get_stock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    resp = requests.get(url).text
    print('%s\n' % resp)


codes = ['sz000878', 'sh600993', 'sz000002', 'sh600153', 'sz002230', 'sh600658' ]
pool = threadpool.ThreadPool(6)
tasks = threadpool.makeRequests(get_stock, codes)
[pool.putRequest(task) for task in tasks]
pool.wait()
b = time.time()
print('consume time is %s s' % (b-a))