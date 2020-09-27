import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com]

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        items = [dict(film_name='电影名称',film_type='电影类型',plan_date='上映日期')]
        print(response.encoding)
        response=response.text.replace("<dd>","</dd><dd>")
        for i in range(1, 11):
            item = SpidersItem()
            film_name = Selector(text=response).xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[1]/span[1]/text()')
            film_type = Selector(text=response).xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[2]/text()')
            plan_date = Selector(text=response).xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[4]/text()')
            # 设置item
            item['film_name'] = film_name.extract_first().strip()
            item['film_type'] = film_type.extract()[1].strip()
            # print(film_type.extract()[1].strip())
            item['plan_date'] = plan_date.extract()[1].strip()
            # print(plan_date.extract()[1].strip())

            items.append(item)
        return items
