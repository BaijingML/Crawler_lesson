import scrapy
# 第三种，把下一页的链接找到，再打开
class JokeSpider(scrapy.Spider):
    name  = 'joke'
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        for joke_class in response.xpath('//*[@class="quote)"]'): # 原Xpath是//*[@id="item_11"]/div[1]/div，去掉数字1之后变成整个列表
            print(joke_class.xpath('span[1]/text()').extract_first)    # 返回列表里的首个元素，得到字符串
            print(joke_class.xpath('span[2]/small/text()').extract_first)

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


