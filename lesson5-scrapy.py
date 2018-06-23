import scrapy

class JulyeduSpider(scrapy.Spider):
    name  = 'julyedu'
    start_urls = ['https://www.julyedu.com/category/index']

    def parse(self, response):
        for julyedu_class in response.xpath('//*[@class="course_info_box)"]'): # 原Xpath是//*[@id="item_11"]/div[1]/div，去掉数字1之后变成整个列表
            print(julyedu_class.xpath('a/h4/text()').extract_first)    # 返回列表里的首个元素，得到字符串
            print(julyedu_class.xpath('a/p[1]/text()').extract_first)
            print(julyedu_class.xpath('a/p[2]/text()').extract_first)
            yield{'title': julyedu_class.xpath('a/h4/text()').extract_first,
                  'discription': julyedu_class.xpath('a/p[1]/text()').extract_first,
                  'time': julyedu_class.xpath('a/p[2]/text()').extract_first}


