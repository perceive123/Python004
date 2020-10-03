import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    # start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)#scrapy自带url去重功能，这里设置为true表示去除url去重功能

    def parse(self, response):
        items = [dict(film_name='电影名称', film_type='电影类型', plan_date='上映日期')]
        movies=Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies[:10]:
            item = MaoyanItem()
            film_name = movie.xpath('.//div[1]/span[1]/text()')
            film_type = movie.xpath('.//div[2]/text()')
            plan_date = movie.xpath('.//div[4]/text()')
        # 设置item
            item['film_name'] = film_name.extract_first().strip()
            # print(film_name.extract_first().strip())
            item['film_type'] = film_type.extract()[1].strip()
            # print(film_type.extract()[1].strip())
            item['plan_date'] = plan_date.extract()[1].strip()
            items.append(item)

        return items
