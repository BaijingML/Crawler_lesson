import requests
from lxml import etree

s = requests.Session()
for id in range(0, 251, 25):
    url = 'http://movie.douban.com/top250/?start-' + str(id)
    r = s.get(url)
    r.encoding = 'utf-8'
    root = etree.HTML(r.content)
    items = root.xpath('//ol/li/div[@class="item"]')
    #print(len(items))
    for item in items:
        title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
        name = title[0].encode('gb2312', 'ingnore').decode('gb2312')   #先编码再解码以过滤其他字符
        #rank  = item.xpath('./div[@class="pic"]/em/text()')[0]
        rate = item.xpath('.//div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        print(name, rate)