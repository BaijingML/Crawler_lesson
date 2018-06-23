import scrapy

# 第二类，拼出连接
class BlogSpider(scrapy.Spider):
    name  = 'cnblog'
    start_urls = ['https://www.cnblogs.com/pick/#p%s' % p for p in range(1,21)]

    def parse(self, response):
        for blog_class in response.xpath('//*[@class=post_item")"]'): # 原Xpath是//*[@id="item_11"]/div[1]/div，去掉数字1之后变成整个列表
            print(blog_class.xpath('div[@class="digg"]/div/span/text()').extract_first)    # 返回列表里的首个元素，得到字符串
            print(blog_class.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first)
            print(blog_class.xpath('div[@class=""]ext()').extract_first)
            yield{'title': blog_class.xpath('a/h4/text()').extract_first,
                  'discription': blog_class.xpath('a/p[1]/text()').extract_first,
                  'time': blog_class.xpath('a/p[2]/text()').extract_first}


